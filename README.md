# Content Creator – LinkedIn personal branding (HR)

| Fil | Indhold |
|-----|---------|
| [content/00-profil.md](content/00-profil.md) | Tines profil, positionering og tone. Grundlaget for alt indhold |
| [content/01-opslagsoversigt.md](content/01-opslagsoversigt.md) | Indholdssøjler, idébank med 45 opslag og aktuelle emner fra LinkedIn, plan for de første 12 uger og spilleregler |
| [content/02-tone-of-voice.md](content/02-tone-of-voice.md) | Tines tone of voice med tjekliste til hvert opslag |
| [content/opslag/](content/opslag/) | Færdige opslag, klar til at poste |
| [content/04-hr-indsigter.md](content/04-hr-indsigter.md) | Nøgletal fra Randstad, Ballisager, Gartner, Deloitte, Korn Ferry, EY, HBR m.fl. med vinkler til opslag |
| [content/03-tal-fra-linkedin.md](content/03-tal-fra-linkedin.md) | Sådan hentes tallene fra LinkedIn i browseren |
| [data/posts.csv](data/posts.csv) | Opslagsplan og reach-data pr. opslag. Det er datakilden til dashboardet |
| [data/profil.csv](data/profil.csv) | Følgere og forbindelser over tid |

**Dashboard:** [Tines LinkedIn-reach](https://claude.ai/artifact/ASFHv1K2J9ooRbCoYCGNue) viser reach pr. opslag. Det er privat, indtil det deles.

**Sådan opdateres tallene:** Ret `data/posts.csv` og `data/profil.csv`, kør `python3 tools/csv_til_json.py build`, og upload de to JSON-filer til dashboardet.

**Næste skridt:** fine-tuning af opslagene.

## Arbejdsgang ved tilretning af opslag

- Vis altid hele opslaget efter hver tilretning, også ved små ændringer, så Tine kan se helheden.
- Alle opslag, kommentarer og svar på kommentarer skal være fri for AI-sprog og i Tines tone, se [tone of voice-guiden](content/02-tone-of-voice.md).
- Ingen spørgsmål til sidst i opslagene.
