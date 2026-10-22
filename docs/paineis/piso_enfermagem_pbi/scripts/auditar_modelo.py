#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "powerbi" / "semantic-model"
TABLES = ROOT / "tables"

def main():
    files = sorted(TABLES.glob("*.tmdl"))
    print(f"Tabelas TMDL: {len(files)}")
    total_cols = total_measures = 0
    for fp in files:
        text = fp.read_text(encoding="utf-8")
        table = re.search(r"^table\s+(.+)$", text, re.M).group(1)
        cols = len(re.findall(r"^\tcolumn\s+", text, re.M))
        measures = len(re.findall(r"^\tmeasure\s+", text, re.M))
        total_cols += cols
        total_measures += measures
        print(f"- {table}: {cols} colunas, {measures} medidas")
    rel_text=(ROOT / "relationships.tmdl").read_text(encoding="utf-8")
    relationships=len(re.findall(r"^relationship\s+", rel_text, re.M))
    print(f"Relacionamentos: {relationships}")
    print(f"Total de colunas: {total_cols}")
    print(f"Total de medidas: {total_measures}")

if __name__ == "__main__":
    main()
