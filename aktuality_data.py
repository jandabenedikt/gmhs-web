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
  fb_url    - (volitelné) odkaz na původní příspěvek na Facebooku; pokud je
              vyplněn, pod textem se zobrazí tlačítko „Zobrazit na Facebooku“
  image     - (volitelné) jméno souboru obrázku uloženého ve složce images/
              (např. "aktualita-priklad.jpg"); pokud je vyplněno, zobrazí se
              pod textem (a případným videem) jako responzivní obrázek
  image_alt - (volitelné) alternativní text k obrázku; není-li uveden,
              použije se jako výchozí hodnota title příspěvku
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
    {
        "slug": "zahajeni-skolniho-roku-2026",
        "fb_url": "https://www.facebook.com/GMHS.ZUS/posts/pfbid0WoKuvYZUKK81qDDxVs9FioTex1prGcfWha7jrESxang4tobgMkBh5Dp1aggrqC1Yl",
        "category": ["gymnazium"],
        "date": "2026-09-01",
        "title": "Zahájení školního roku v duchu džungle",
        "excerpt": "Nové studenty přivítali letošní oktaváni školním pralesem, úkoly a domorodou snídaní.",
        "body_html": (
            '<p class="aktualita-text">Tradiční zahájení školního roku v atriu Gymnázia a Hudební školy '
            'hl. m. Prahy okořenili letošní oktaváni tématem džungle. Po projití "školním pralesem", '
            'splnění řady úkolů a ochutnávce domorodé snídaně uvítala nové studenty prim celá škola '
            'v čele s ředitelem Filipem Magramem. Moc se na ně těšíme a přejeme hodně úspěchů, '
            'nejen těch studijních a hudebních❤️</p>'
        ),
    },
    {
        "slug": "ema-adamkova-viden",
        "fb_url": "https://www.facebook.com/GMHS.ZUS/posts/pfbid02WCAFC4dsx5eMd9JrYT8YM9SADMVszooxgLCpcCK8j9g3hwBgJXPofDfBVQdYupcpl",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-09-03",
        "title": "Ema Adamková vítězkou kytarové soutěže ve Vídni",
        "excerpt": "Studentka GMHS Ema Adamková zvítězila v mezinárodní kytarové soutěži ve Vídni.",
        "body_html": (
            '<p class="aktualita-text">Vynikající úspěch studentky GMHS Emy Adámkové, GRATULUJEME!!!</p>\n'
            '      <p class="aktualita-text"><a href="https://www.klasikaplus.cz/ema-adamkova-vitezkou-mezinarodni-kytarove-souteze-ve-vidni/" '
            'target="_blank" rel="noopener">Ema Adamková vítězkou mezinárodní kytarové soutěže ve Vídni</a></p>'
        ),
    },
    {
        "slug": "koncertni-sezona-zlonice",
        "fb_url": "https://www.facebook.com/GMHS.ZUS/posts/pfbid0U55gEsx37JfgSnk2MB4vsjqAXvuh8wZQf3GqpH5Lq9xrNWQvNjNfGfgxEV1uZve6l",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-09-15",
        "title": "Koncertní sezonu začínáme ve Zlonicích",
        "excerpt": "Novou koncertní sezonu tradičně zahajujeme u Antonína Dvořáka ve Zlonicích.",
        "body_html": (
            '<p class="aktualita-text">Koncertní sezonu začínáme tradičně ve Zlonicích u Antonína Dvořáka.</p>'
        ),
    },
    {
        "slug": "pocta-antoninu-dvorakovi",
        "fb_url": "https://www.facebook.com/GMHS.ZUS/posts/pfbid0mWaumzJdfnx3mw7p5Um5sRJBiScpfh7xpiTP9kLtu2881B9tq6WEVfLwtWDLBmE3l",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-09-20",
        "title": "Pocta Antonínu Dvořákovi",
        "excerpt": "Ohlédnutí za koncertem ve Zlonicích, kterým jsme zahájili novou koncertní sezonu.",
        "body_html": (
            '<p class="aktualita-text">Gratulujeme žákům gymnázia a hudební školy ke krásnému koncertu! '
            'Díla nejen Dvořáka, ale i Beethovena, Liszta a dalších předvedli: Evelína Klasnová (HŠ), '
            'Helena Vydrová (sexta), Ondřej Skopový (sekunda), Matouš Zaplatílek (septima), '
            'Luna Hovorková (kvinta), Ondřej Petrášek (oktáva) a Viola Lukášová (septima).</p>\n'
            '      <p class="aktualita-text">Speciální díky Pavel Voráček za klavírní spolupráci celým programem 🌹</p>'
        ),
    },
    {
        "slug": "pisnova-soutez-bohuslava-martinu",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-10-13",
        "title": "Písňová soutěž Bohuslava Martinů",
        "excerpt": "24. ročník písňové soutěže B. Martinů je tady!",
        "body_html": (
            '<p class="aktualita-text">16. – 18. října proběhne na naší škole v prostorách již '
            '24. ročník pěvecké soutěže.</p>\n'
            '      <div class="aktualita-video" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">\n'
            '        <iframe src="https://www.youtube.com/embed/nsrhBdMw7vI" title="YouTube video" '
            'style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'allowfullscreen loading="lazy"></iframe>\n'
            '      </div>'
        ),
    },
    {
        "slug": "koncert-100-let-janzurova",
        "category": ["gymnazium"],
        "date": "2026-10-26",
        "title": "Koncert k nedožitým 100. narozeninám prof. Zdeny Janžurové",
        "excerpt": "Videopozvánka na hudební večer k poctě Zdeny Janžurové a jejímu celoživotnímu úsilí předávat radost z hudby dalším generacím.",
        "body_html": (
            '<p class="aktualita-text">Zdena Janžurová byla klavírní pedagožka a autorka odborných '
            'a výukových publikací. Společně s Miladou Borovou vytvořila známé české učebnice pro děti, '
            'například Klavírní školičku a čtyřdílnou Novou klavírní školu (včetně dílu Nová klavírní '
            'škola 1), které slouží k výuce začínajících klavíristů. Její profily a tvorbu můžete najít '
            'na Databázi knih, nebo v katalogu na Městská knihovna v Praze.</p>\n'
            '      <div class="aktualita-video" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">\n'
            '        <iframe src="https://www.youtube.com/embed/eY_jKYFtlEw" title="YouTube video" '
            'style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'allowfullscreen loading="lazy"></iframe>\n'
            '      </div>'
        ),
        "image": "aktualita-janzurova-koncert.jpg",
    },
    {
        "slug": "konkurz-fok",
        "category": ["gymnazium"],
        "date": "2026-10-26",
        "title": "Konkurz na sólistu se Symfonickým orchestrem Hlavního města Prahy, FOK",
        "excerpt": "Veřejný konkurz na sólistu slavnostního koncertu s orchestrem FOK — přihlášky do 8. ledna 2027.",
        "body_html": (
            '<p class="aktualita-text">Veřejný konkurz na sólistu slavnostního koncertu se Symfonickým '
            'orchestrem hl. m. Prahy FOK se uskuteční v úterý 16. února 2027 v Koncertním sále školy. '
            'Samotný slavnostní koncert se bude konat 29. dubna 2027 ve Smetanově síni Obecního domu. '
            'Podmínky konkurzu jsou uvedeny na stránkách GMHS.</p>'
        ),
        "image": "aktualita-konkurz-fok.jpg",
    },
    {
        "slug": "den-otevrenych-dveri",
        "category": ["gymnazium"],
        "date": "2026-10-26",
        "title": "Den otevřených dveří",
        "excerpt": "Zveme zájemce o studium na Den otevřených dveří 26. 11. 2026 a 21. 1. 2027 — prohlídka školy i výuky.",
        "body_html": (
            '<p class="aktualita-text">26. listopadu 2026 se koná první den otevřených dveří, '
            'druhý termín je pak 21. ledna 2027. Zveme všechny zájemce o studium na GMHS k prohlídce '
            'nejen budovy, ale i k návštěvě vyučování. Prohlídka školy za doprovodu studentů probíhá '
            'od 15:30 do 18:00, s vedením školy pak od 17:00 do 18:00 v Koncertním sále.</p>'
        ),
        "image": "aktualita-den-otevrenych-dveri.jpg",
    },
    {
        "slug": "ohlednuti-zari-rijen-2026",
        "category": ["gymnazium"],
        "date": "2026-11-02",
        "title": "Ohlédnutí za začátkem školního roku 2026 / 2027",
        "excerpt": "Krátká shrnující videa prezentující nejvýraznější události ze života školy za září a říjen.",
        "body_html": (
            '<p class="aktualita-text">U nás to žije od prvního dne školy! Pojďte se podívat na výběr '
            'nejvýraznějších momentů a akcí za září a říjen!</p>\n'
            '      <p class="aktualita-text" style="font-weight:600;margin-top:18px;margin-bottom:8px;">'
            'Ohlédnutí za uplynulým měsícem září</p>\n'
            '      <div class="aktualita-video" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">\n'
            '        <iframe src="https://www.youtube.com/embed/vk9cINKyLYw" title="Ohlédnutí za uplynulým měsícem září" '
            'style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'allowfullscreen loading="lazy"></iframe>\n'
            '      </div>\n'
            '      <p class="aktualita-text" style="font-weight:600;margin-top:18px;margin-bottom:8px;">'
            'Ohlédnutí za uplynulým měsícem na GMHS říjen 2026</p>\n'
            '      <div class="aktualita-video" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">\n'
            '        <iframe src="https://www.youtube.com/embed/lC1PZSBzfdc" title="Ohlédnutí za uplynulým měsícem na GMHS říjen 2026" '
            'style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'allowfullscreen loading="lazy"></iframe>\n'
            '      </div>'
        ),
    },
    {
        "slug": "30-let-spolu",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-11-02",
        "title": "30 let spolu!",
        "excerpt": "Koncert k 30 letům Hudební školy a Gymnázia hlavního města Prahy na Komenského náměstí. Symfonický orchestr GMHS se sólistou Tomášem Jamníkem zahrají v kostele sv. Šimona a Judy",
        "body_html": (
            '<p class="aktualita-text">GMHS slaví jubileum! A to stylově koncertem svého Symfonického '
            'orchestru Gymnázia a Hudební školy hlavního města Prahy se sólistou Tomášem Jamníkem. '
            'Pátek 13. listopadu, kostel sv. Šimona a Judy, 19.00.</p>\n'
            '      <p class="aktualita-text">Název koncertu 30 let spolu není nahodilý. Tak dlouho '
            'totiž sídlí Hudební škola a Gymnázium hlavního města Prahy společně jako jedna velká '
            'hudební rodina na Komenského náměstí na Žižkově. Ze snu ve skutečnost se tak proměnila '
            'myšlenka Jana Vychytila, někdejšího ředitele vzorové školy ZUŠ Voršilská, který toužil '
            'založit gymnázium, které by vedle vysoké úrovně hudební zajistilo také kvalitní vzdělání '
            'všeobecné. Koncert tak připomeneme i nedožité 80. výročí jeho narození</p>\n'
            '      <p class="aktualita-text">Třicet let, to je důvod i k malé bilanci a také '
            'k setkávání. Samotnému koncertu proto bude jako preludium předcházet debata s absolventy '
            'Gymnázia a Hudební školy – zpěvačkou a harfistkou Hanou Blažíkovou, violoncellistkou '
            'Dominikou Weiss Hoškovou a Tomášem Jamníkem, která se uskuteční ve středu 11. listopadu '
            'v 18 hodin v Koncertním sále školy. Ve čtvrtek 12. listopadu potom Hana Blažíková a '
            'Tomáš Jamník povedou v Koncertním a Komorním sále školy masterclass. Všechny akce jsou '
            'otevřeny i široké veřejnosti. Vstup zdarma.</p>\n'
            '      <p class="aktualita-text"><a href="https://www.klasikaplus.cz/gymnazium-a-hudebni-skola-hl-mesta-prahy-oslavi-tricet-let-spolecneho-pusobeni/" '
            'target="_blank" rel="noopener">Gymnázium a Hudební škola hl. města Prahy oslaví třicet let '
            'společného působení</a></p>\n'
            '      <p class="aktualita-text" style="font-weight:600;margin-top:18px;margin-bottom:4px;">'
            'Program koncertu</p>\n'
            '      <p class="aktualita-text" style="margin-bottom:4px;">Antonín Dvořák: Legendy, '
            'op. 59 (č. 3 Allegro giusto)</p>\n'
            '      <p class="aktualita-text" style="margin-bottom:4px;">Antonín Dvořák: Slovanské '
            'tance, op. 46 (č. 7 „Skočná“)</p>\n'
            '      <p class="aktualita-text" style="margin-bottom:4px;">Josef Suk: Jaro, op. 22a, '
            'č. 5. V roztoužení (instrum. Anatol Provazník)</p>\n'
            '      <hr style="border:none;border-top:1px solid var(--bg-alt);margin:14px 0;">\n'
            '      <p class="aktualita-text">Antonín Dvořák: Koncert pro violoncello a orchestr '
            'h moll, op. 104, B191</p>\n'
            '      <div class="aktualita-video" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">\n'
            '        <iframe src="https://www.youtube.com/embed/yEh7L1o5Cj0" title="30 let spolu" '
            'style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'allowfullscreen loading="lazy"></iframe>\n'
            '      </div>'
        ),
        "image": "aktualita-30-let-spolu.jpg",
    },
    {
        "slug": "gmhs-slavi-tri-akce",
        "category": ["gymnazium", "hudebni-skola"],
        "date": "2026-11-02",
        "title": "GMHS slaví! Setkání, masterclassy, koncert",
        "excerpt": "Přijďte na uvolněné setkání s absolventy GMHS i na jejich následný masterclass.",
        "body_html": (
            '<p class="aktualita-text">30 let spolu! GMHS slaví koncertem s Tomášem Jamníkem '
            'a masterclassy s Hanou Blažíkovou</p>\n'
            '      <p class="aktualita-text">Třicet let společné existence Gymnázia a Hudební '
            'školy hlavního města Prahy pod jednou střechou jako jedné velké hudební rodiny, to je '
            'důvod i k malé bilanci a také k setkávání. Oslavy začnou malým preludiem - debatou '
            's absolventy Gymnázia a Hudební školy – zpěvačkou a harfistkou Hanou Blažíkovou, '
            'violoncellistkou Dominikou Weiss Hoškovou a violoncellistou Tomášem Jamníkem, která se '
            'uskuteční ve středu 11. listopadu v 18 hodin v Koncertním sále školy. Ve čtvrtek '
            '12. listopadu potom Hana Blažíková a Tomáš Jamník povedou v Koncertním a Komorním sále '
            'školy masterclass. Oslavy potom vyvrcholí koncertem Symfonického orchestru GMHS se '
            'sólistou Tomášem Jamníkem, pod taktovkou Petra Jiříkovského v pátek 13. listopadu '
            'v kostele sv. Šimona a Judy.</p>\n'
            '      <p class="aktualita-text">Všechny akce jsou otevřeny i široké veřejnosti. '
            'Vstup zdarma.</p>'
        ),
        "image": "aktualita-gmhs-slavi-tri-akce.jpg",
    },
]
