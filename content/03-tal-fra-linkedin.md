# Sådan hentes tallene fra LinkedIn (browser-tjek)

Til en Claude-session, der kører på Tines egen computer og kan bruge en browser, hvor Tine er logget ind på LinkedIn.

## Hvornår

7 dage efter hvert opslag er postet, og en gang om måneden for antal følgere.

## Hvad der læses (kun Tines egne tal, kun læsning)

1. Åbn Tines profil → **Aktivitet** → **Opslag**.
2. For hvert opslag, der er postet, men endnu ikke målt (`status` er ikke `postet`, eller `maalt_dato` er tom i `data/posts.csv`): klik **Vis analyse**, og notér
   - eksponeringer
   - reaktioner
   - kommentarer
   - genopslag
   - profilvisninger fra opslaget (hvis det vises)
   - nye følgere fra opslaget (hvis det vises)
3. Notér antal **følgere** og **forbindelser** fra profilen.

Der klikkes, likes, kommenteres og postes ikke. Der læses kun.

## Hvad der opdateres

1. `data/posts.csv`: sæt `status` til `postet`, og udfyld `dato`, `maalt_dato` og tallene.
2. `data/profil.csv`: tilføj en ny linje med dato, følgere og forbindelser.
3. Kør `python3 tools/csv_til_json.py build`.
4. Upload `build/opslag.json` og `build/profil.json` til dashboardet [Tines LinkedIn-reach](https://claude.ai/artifact/ASFHv1K2J9ooRbCoYCGNue) som assets, og opdatér `source.url` og `updated` i dokumenterne `datasets/opslag` og `datasets/profil`.
5. Commit og push til branchen `claude/linkedin-content-strategy-azqlka`.
6. Fortæl Tine kort, hvad tallene viser.
