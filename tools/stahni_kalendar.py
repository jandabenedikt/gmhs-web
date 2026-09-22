#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stáhne iCal feed akcí ze systému Klasifikace a uloží ho jako data/akce.json,
ze kterého stránka kalendar-akci.html (skript kalendar.js) vykresluje akce.

Spouští ho automaticky GitHub Actions (.github/workflows/kalendar-akci.yml).
Jde spustit i ručně:  python3 tools/stahni_kalendar.py
Pro test z lokálního souboru:  python3 tools/stahni_kalendar.py soubor.ics

Používá jen standardní knihovnu Pythonu (bez instalace balíčků).
"""
import json
import os
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

FEED_URL = "https://klasifikace.jphsw.cz/calendar/ical/?hash=6da9003b743b65f4c0ccd295cc484e57"
LOCAL_TZ = ZoneInfo("Europe/Prague")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "data", "akce.json")


def load_ics(source=None):
    if source:
        with open(source, "rb") as f:
            raw = f.read()
    else:
        req = urllib.request.Request(FEED_URL, headers={"User-Agent": "gmhs.cz kalendar-akci"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
    return raw.decode("utf-8-sig", errors="replace")


def unfold(text):
    """Spojí zalomené řádky podle RFC 5545 (pokračovací řádek začíná mezerou/tabulátorem)."""
    lines = []
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if line[:1] in (" ", "\t") and lines:
            lines[-1] += line[1:]
        else:
            lines.append(line)
    return lines


def parse_line(line):
    """'DTSTART;TZID=Europe/Prague:20260923T180000' -> ('DTSTART', {'TZID': ...}, '2026...')"""
    in_quotes = False
    for i, ch in enumerate(line):
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == ":" and not in_quotes:
            head, value = line[:i], line[i + 1:]
            break
    else:
        return None
    parts = head.split(";")
    params = {}
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            params[k.upper()] = v.strip('"')
    return parts[0].upper(), params, value


def unescape(value):
    out, i = [], 0
    while i < len(value):
        ch = value[i]
        if ch == "\\" and i + 1 < len(value):
            nxt = value[i + 1]
            out.append("\n" if nxt in "nN" else nxt)
            i += 2
        else:
            out.append(ch)
            i += 1
    return "".join(out).strip()


def parse_dt(value, params):
    """Vrátí (datetime v místním čase nebo date, all_day)."""
    value = value.strip()
    if params.get("VALUE") == "DATE" or (len(value) == 8 and value.isdigit()):
        return date(int(value[0:4]), int(value[4:6]), int(value[6:8])), True
    dt = datetime.strptime(value[:15], "%Y%m%dT%H%M%S")
    if value.endswith("Z"):
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        tzid = params.get("TZID")
        try:
            dt = dt.replace(tzinfo=ZoneInfo(tzid) if tzid else LOCAL_TZ)
        except Exception:
            dt = dt.replace(tzinfo=LOCAL_TZ)
    return dt.astimezone(LOCAL_TZ).replace(tzinfo=None), False


def parse_events(text):
    events, cur = [], None
    for line in unfold(text):
        if line == "BEGIN:VEVENT":
            cur = {}
            continue
        if line == "END:VEVENT":
            if cur is not None:
                events.append(cur)
            cur = None
            continue
        if cur is None:
            continue
        parsed = parse_line(line)
        if not parsed:
            continue
        name, params, value = parsed
        if name in ("DTSTART", "DTEND"):
            try:
                cur[name] = parse_dt(value, params)
            except ValueError:
                pass
        elif name in ("SUMMARY", "LOCATION", "DESCRIPTION", "URL", "UID", "STATUS"):
            cur[name] = unescape(value)
        elif name == "DURATION":
            cur[name] = value
    return events


def parse_duration(value):
    """Jednoduchý převod ISO 8601 trvání (např. PT1H30M, P1D) na timedelta."""
    import re
    m = re.fullmatch(r"([+-])?P(?:(\d+)W)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?", value or "")
    if not m:
        return None
    sign = -1 if m.group(1) == "-" else 1
    w, d, h, mi, s = (int(x) if x else 0 for x in m.groups()[1:])
    return sign * timedelta(weeks=w, days=d, hours=h, minutes=mi, seconds=s)


def to_json_event(ev):
    if "DTSTART" not in ev or ev.get("STATUS", "").upper() == "CANCELLED":
        return None
    start, all_day = ev["DTSTART"]
    end = ev.get("DTEND", (None, all_day))[0]
    if end is None and ev.get("DURATION"):
        dur = parse_duration(ev["DURATION"])
        if dur is not None:
            end = start + dur
    if all_day:
        # DTEND je u celodenních akcí podle standardu exkluzivní -> poslední den = DTEND - 1 den
        last = (end - timedelta(days=1)) if isinstance(end, date) and end > start else start
        return {
            "title": ev.get("SUMMARY", "") or "Akce",
            "allDay": True,
            "start": start.isoformat(),
            "end": last.isoformat(),
            "location": ev.get("LOCATION", ""),
            "description": ev.get("DESCRIPTION", ""),
            "url": ev.get("URL", ""),
        }
    return {
        "title": ev.get("SUMMARY", "") or "Akce",
        "allDay": False,
        "start": start.isoformat(timespec="minutes"),
        "end": end.isoformat(timespec="minutes") if isinstance(end, datetime) else None,
        "location": ev.get("LOCATION", ""),
        "description": ev.get("DESCRIPTION", ""),
        "url": ev.get("URL", ""),
    }


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else None
    text = load_ics(source)
    if "BEGIN:VCALENDAR" not in text:
        sys.exit("Stažený soubor nevypadá jako iCal kalendář — data/akce.json se nemění.")
    events = [e for e in (to_json_event(ev) for ev in parse_events(text)) if e]
    events.sort(key=lambda e: (e["start"], e["title"]))
    payload = {"events": events}

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    new = json.dumps(payload, ensure_ascii=False, indent=1)
    old = None
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH, encoding="utf-8") as f:
            old = f.read()
    if old == new:
        print(f"Beze změny ({len(events)} akcí).")
        return
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(new)
    print(f"Uloženo {len(events)} akcí do data/akce.json.")


if __name__ == "__main__":
    main()
