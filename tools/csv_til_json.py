"""Konverterer data/posts.csv og data/profil.csv til JSON-filerne, som dashboardet læser.

Kør fra repoets rod:  python3 tools/csv_til_json.py <output-mappe>
Upload derefter opslag.json og profil.json til dashboardet.
"""
import csv
import json
import sys
from pathlib import Path

TAL = {"eksponeringer", "reaktioner", "kommentarer", "genopslag", "profilvisninger", "nye_foelgere", "henvendelser"}


def main(out_dir: str) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    opslag = []
    with open("data/posts.csv", encoding="utf-8") as f:
        for i, r in enumerate(csv.DictReader(f)):
            row = {k: (int(v) if k in TAL and v else (v or None)) for k, v in r.items()}
            row["raekkefoelge"] = i + 1
            opslag.append(row)

    with open("data/profil.csv", encoding="utf-8") as f:
        profil = [{k: (v if k == "dato" else int(v)) for k, v in r.items()} for r in csv.DictReader(f)]

    (out / "opslag.json").write_text(json.dumps(opslag, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "profil.json").write_text(json.dumps(profil, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "build")
