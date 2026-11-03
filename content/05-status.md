# Status og overlevering

> Læs denne fil først i hver ny samtale. Den fortæller, hvor vi er, og hvilke regler der gælder.
> Opdateres, hver gang en samtale afsluttes. Senest opdateret: 3. november 2026.

## Regler, Tine har sat (gælder altid)

- Alle opslag, kommentarer og svar er på dansk, i Tines tone ([tone of voice](02-tone-of-voice.md)) og fri for AI-sprog.
- 1 opslag om ugen, tirsdag kl. 8.30. Tine poster selv.
- Intet spørgsmål til sidst i opslag.
- Vis altid HELE opslaget efter hver rettelse.
- Gå opslag igennem afsnit for afsnit med 2–3 muligheder og en anbefaling.
- Forklar teknik enkelt, "som til en 8-årig".
- Peakon: "gennemsnit 8,4 mod en benchmark på 7,7". Frivillig personaleomsætning: "omkring 10 %".
- Ét tal pr. opslag, og altid med Tines egen erfaring ved siden af.
- Højst 3 hashtags. ⚖️ til dilemma-serien, 💙 som signatur.
- Brug ikke Nordvik-filen. Ingen interne Randstad-forhold (fritstillet til 28/2-2027). Repoet er offentligt: ingen adresse, telefon, ansøgninger eller kontaktpersoner.
- Løngennemsigtighed venter til loven er vedtaget (planlagt 1/3-2027).
- Grafik i bannerfarverne: navy #16304f → blå #1f6fa3, rød accent #e2483c. Bredt format 1200 x 627.
- Claude skal selv foreslå en ny samtale, når samtalen er blevet lang, og opdatere denne fil først.

## Hvor vi er

| Uge | Opslag | Status |
|-----|--------|--------|
| 42 | Facade eller ej? | Postet 13/10, målt |
| 43 | Ekspert i alt, specialist i intet? ⚖️ | Postet 20/10, målt |
| 44 | Tidligere MUS-jæger 🙈 | Postet 27/10, målt |
| 45 | Agenten blev, da medarbejderen gik 🤖 (med grafik) | Postet 3/11, måles 10/11 |
| 46 | Dilemma 2: Hvem er HR's kunde? (afstemning) | Næste. Ikke skrevet endnu |

Resten af planen står i [opslagsoversigten](01-opslagsoversigt.md).

## Det har vi lært af tallene

- Opslag med en holdning, folk kan genkende sig selv i, giver flest kommentarer (Facade: 20). Fortællinger giver reaktioner, men få kommentarer.
- Profilvisninger kommer mest fra opslag om Tine selv og hendes jobsøgning (Netflix-opslaget: 186). Forslag: et "sæson 4"-opslag om måneden.
- Tine skriver selv den første kommentar (fx kilden) og fastgør den.

## Faste opgaver

- **Tirsdag før 8.30:** vis den endelige tekst, mind om at kommentere hos 3–5 andre.
- **7 dage efter et opslag:** Tine sender skærmbillede af "Vis analyse". Opdatér `data/posts.csv`, kør `python3 tools/csv_til_json.py <mappe>`, upload `opslag.json` som asset til [dashboardet](https://claude.ai/artifact/ASFHv1K2J9ooRbCoYCGNue), opdatér `datasets/opslag` (source.url og updated), slet det gamle asset, commit og push.
- **Den 1. i måneden:** opdatér [HR-indsigter](04-hr-indsigter.md).
- Push altid til branchen `claude/linkedin-content-strategy-azqlka` (kør `git pull --rebase` først).

## Påmindelser, der skal flyttes til den nye samtale

De planlagte påmindelser er bundet til den gamle samtale. I en ny samtale: opret dem igen og slet de gamle.
- Tal for uge 45: tirsdag 10/11 kl. 16 (dansk tid).
- Månedlig HR-indsigt: den 1. kl. 8.55 (dansk tid).
- Postedag-påmindelse: hver tirsdag kl. 7.15 (dansk tid).
