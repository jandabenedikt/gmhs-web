#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datový zdroj pro sekci Aktuality.

Nový příspěvek se přidá jako další slovník do seznamu AKTUALITY níže.
Po úpravě spusťte `python3 generate_pages.py` — znovu se vygeneruje stránka
o-nas/aktuality.html i náhledové boxy s aktualitami na úvodní stránce
(automaticky se zobrazí 3 nejnovější příspěvky, řazeno podle data sestupně;
při stejném datu zůstávají příspěvky v pořadí, v jakém jsou zapsané níže).

Pole u každého příspěvku:
  slug      - jedinečný identifikátor (bez diakritiky a mezer), použije se
              jako kotva v URL (o-nas/aktuality.html#slug)
  category  - seznam s jednou nebo oběma hodnotami "gymnazium" a
              "hudebni-skola" — určuje štítek/y nad nadpisem. Barevné
              odlišení oddílu na stránce Aktuality dostává tmavší odstín
              pouze příspěvek s jedinou kategorií ["gymnazium"], všechny
              ostatní (samotná "hudebni-skola" i oba štítky současně)
              mají základní (světlejší) odstín pozadí webu.
  date      - datum ve formátu "RRRR-MM-DD" (podle něj se řadí, nejnovější nahoře)
  title     - nadpis příspěvku
  excerpt   - krátký popis (1–2 věty) pro box na úvodní stránce
  body_html - plný text příspěvku (HTML, typicky jeden nebo více
              odstavců s třídou "aktualita-text")
"""

AKTUALITY = [
    {
        "slug": "zaciname",
        "category": ["gymnazium"],
        "date": "2026-08-28",
        "title": "Začínáme!",
        "excerpt": "V úterý 1. 9. 2026 společně zahájíme nový školní.",
        "body_html": (
            '<p class="aktualita-text">V úterý 1. 9. 2026 společně zahájíme nový školní rok '
            'a zároveň přivítáme žáky prim. Jako každý rok, tak i letos se mohou žáci těšit '
            'na výpravné přivítání, které si připravili žáci oktáv.</p>\n'
            '      <p class="aktualita-text">Na to, jak první školní den vypadal před rokem '
            'se můžete podívat v <a href="https://www.rajce.idnes.cz/avuwalub/album/2025-09-01-zacatek-skolniho-roku" '
            'target="_blank" rel="noopener">galerii</a>.</p>'
        ),
    },
    {
        "slug": "novy-web",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-08-28",
        "title": "Nový web",
        "excerpt": "Došlo k vizuální obměně a reorganizaci webu.",
        "body_html": (
            '<p class="aktualita-text">S novým školním rokem spouštíme i nový web školy. '
            'V první fázi bylo reorganizovat obsah webu původního a dát mu nový grafický háv. '
            'Postupně budeme přidávat nové funkce i nový obsah. Proto bychom Vás rádi poprosili '
            'o zpětnou vazbu.</p>\n'
            '      <p class="aktualita-text">Vyplňte prosím krátký dotazník (1 min.) na '
            '<a href="https://forms.gle/nyZUg3oy5QUhtQn67" target="_blank" rel="noopener">tomto odkaze</a>.</p>\n'
            '      <p class="aktualita-text">Předem děkujeme za Váš čas :)</p>'
        ),
    },
]
