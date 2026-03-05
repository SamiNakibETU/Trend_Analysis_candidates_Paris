#!/usr/bin/env python3
"""Extrait TOUTES les sorties stdout des notebooks A1-A7."""
import json
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / "A7_synthese" / "outputs" / "FINDINGS_EXHAUSTIF_A1_A7.md"

NOTEBOOKS = [
    "A1_temporal/A1_temporal.ipynb",
    "A2_topics/A2_topics.ipynb",
    "A3_sentiment/A3_sentiment.ipynb",
    "A4_community/A4_community.ipynb",
    "A5_interactions/A5_interactions.ipynb",
    "A6_bert_finetuning/A6_bert_finetuning.ipynb",
    "A7_synthese/A7_synthese.ipynb",
]

def extract_stdout(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    blocks = []
    for i, cell in enumerate(nb.get("cells", [])):
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream" and out.get("name") == "stdout":
                text = "".join(out.get("text", []))
                if text.strip():
                    blocks.append(text)
    return blocks

def main():
    md = []
    md.append("# FINDINGS EXHAUSTIFS — Paris Municipales 2026")
    md.append("**TOUTES les sorties chiffrées des notebooks A1 à A7**")
    md.append("")
    md.append("---")
    md.append("")

    for nb_path in NOTEBOOKS:
        path = BASE / nb_path
        if not path.exists():
            md.append(f"## {Path(nb_path).parent.name} — Fichier non trouvé")
            md.append("")
            continue

        name = Path(nb_path).parent.name
        md.append(f"# {name}")
        md.append("")
        blocks = extract_stdout(path)
        for j, block in enumerate(blocks):
            md.append("```")
            md.append(block.rstrip())
            md.append("```")
            md.append("")
        md.append("---")
        md.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(md), encoding="utf-8")
    print(f"Écrit : {OUT}")
    total = sum(len(extract_stdout(BASE / p)) for p in NOTEBOOKS if (BASE / p).exists())
    print(f"Total blocs extraits : {total}")

if __name__ == "__main__":
    main()
