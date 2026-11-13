# Status og overlevering

> Læs denne fil først i hver ny samtale. Den fortæller, hvor vi er, og hvilke regler der gælder.
> Opdateres, hver gang en samtale afsluttes. Senest opdateret: 13. november 2026.

## Regler, Tine har sat (gælder altid)

- Alle opslag, kommentarer og svar er på dansk, i Tines tone ([tone of voice](02-tone-of-voice.md)) og fri for AI-sprog.
- 1 opslag om ugen, tirsdag kl. 8.30. Tine poster selv.
- Intet spørgsmål til sidst i opslag.
- Vis altid HELE opslaget efter hver rettelse.
- Gå opslag igennem afsnit for afsnit med 2–3 muligheder og en anbefaling.
- Forklar teknik enkelt, "som til en 8-årig".
- Peakon: "gennemsnit 8,4 mod en benchmark på 7,7". Frivillig turnover: "omkring 10 %" (Tine foretrækker "turnover" frem for "personaleomsætning").
- Brug ikke undersøgelser eller tal fra 2024 (eller ældre), heller ikke "faldet siden 2024". Tine anser dem ikke for valide.
- Ingen afstemninger i opslagene (heller ikke i dilemma-serien).
- Tine sidder/sad selv i ledergruppen: skriv "vi" / "os i ledergruppen", ikke "ledelsen", når hun var med til beslutningen.
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
| 45 | Agenten blev, da medarbejderen gik 🤖 (med grafik) | Postet 3/11, målt 10/11 (1.071 eksponeringer) |
| 46 | Tre svar. Kun ét var rigtigt. ⚖️ (dilemma 2, ren tekst) | Postet 11/11 ([se opslaget](opslag/uge46-hr-kunde.md)). Måles 17/11 (efter 6 dage) |
| 47 | C5 – Mit eget jobopslag (A9 udskudt) | Udkast 3 med Netflix-rammen under gennemgang, postes 17/11 kl. 8.30 ([se opslaget](opslag/uge47-mit-eget-jobopslag.md)) |

Resten af planen står i [opslagsoversigten](01-opslagsoversigt.md).

## Det har vi lært af tallene

- Opslag med en holdning, folk kan genkende sig selv i, giver flest kommentarer (Facade: 20). Fortællinger giver reaktioner, men få kommentarer.
- Profilvisninger kommer mest fra opslag om Tine selv og hendes jobsøgning (Netflix-opslaget: 186). Forslag: et "sæson 4"-opslag om måneden.
- Uge 45 (eneste opslag med grafik) nåede kun 1.071 og 33 % uden for netværket (normalt 65–79 %), men havde den højeste andel kommentarer (7). Ét datapunkt; derfor ren tekst i uge 46.
- Tine skriver selv den første kommentar (fx kilden) og fastgør den.

## Faste opgaver

- **Tirsdag før 8.30:** vis den endelige tekst, mind om at kommentere hos 3–5 andre.
- **7 dage efter et opslag:** Tine sender skærmbillede af "Vis analyse". Opdatér `data/posts.csv`, kør `python3 tools/csv_til_json.py <mappe>`, upload `opslag.json` som asset til [dashboardet](https://claude.ai/artifact/ASFHv1K2J9ooRbCoYCGNue), opdatér `datasets/opslag` (source.url og updated), slet det gamle asset, commit og push.
- **Den 1. i måneden:** opdatér [HR-indsigter](04-hr-indsigter.md).
- Push altid til branchen `claude/linkedin-content-strategy-azqlka` (kør `git pull --rebase` først).

## Påmindelser

Påmindelserne er bundet til samtalen session_01ASyS4CCKDwbJ8mNK9TtjCC (flyttet 13/11). Starter du en ny samtale: opret dem igen der og slet de gamle.
- Tal for uge 46: tirsdag 17/11 kl. 16 (dansk tid).
- Månedlig HR-indsigt: den 1. kl. 8.55 (dansk tid).
- Postedag-påmindelse: hver tirsdag kl. 7.15 (dansk tid).
