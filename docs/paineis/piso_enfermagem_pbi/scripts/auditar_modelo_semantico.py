#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "powerbi" / "semantic-model"
TABLES = ROOT / "tables"

findings = []

def add(severity, code, message):
    findings.append((severity, code, message))

all_text = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.rglob("*.tmdl"))

if re.search(r'File\.Contents\("[A-Za-z]:\\', all_text):
    add("P1", "ABSOLUTE_PATH", "Há File.Contents() com caminho absoluto local.")

if "LocalDateTable_" in all_text:
    add("P2", "AUTO_DATE_TIME", "LocalDateTable_* detectada; existe calendário automático além de dim_data.")

if "Erros em Repasses" in all_text:
    count = len(re.findall(r"expression 'Erros em Repasses", all_text))
    add("P2", "ERROR_QUERIES", f"Foram detectadas {count} queries de troubleshooting 'Erros em Repasses*'.")

for fn in ["Repasses.tmdl", "Piso_Enfermagem.tmdl"]:
    txt = (TABLES/fn).read_text(encoding="utf-8")
    if re.search(r'column Codigo_OS\s*=.*IF\(', txt):
        add("P1", "HARDCODED_OS_MAPPING", f"{fn}: Codigo_OS é mapeado em DAX por IF hardcoded.")
    if re.search(r'Codigo_OS\s*=.*\b0\)', txt):
        add("P1", "ZERO_FALLBACK", f"{fn}: mapping de OS possui fallback 0.")

# Verifica a origem da dimensão de instituição
inst = (TABLES/'dim_institui#U00e7#U00e3o.tmdl').read_text(encoding='utf-8')
if 'SELECTCOLUMNS(\n\t\t\t\t        Repasses' in inst or re.search(r'SELECTCOLUMNS\(\s*Repasses', inst, re.S):
    add("P1", "DIM_INSTITUTION_COVERAGE", "dim_instituição é derivada somente de Repasses.")

# Compara os tipos das chaves de OS
def dtype(file, col):
    txt=(TABLES/file).read_text(encoding='utf-8')
    pat=rf'^\tcolumn\s+{re.escape(col)}(?:\s*=.*)?$'
    m=re.search(pat, txt, re.M)
    if not m: return None
    tail=txt[m.end():]
    next_m=re.search(r'^\t(?:column|partition)\s+', tail, re.M)
    block=tail[:next_m.start()] if next_m else tail
    d=re.search(r'^\t\tdataType:\s*(\S+)', block, re.M)
    return d.group(1) if d else 'inferred'

types = {
    'Repasses.Codigo_OS': dtype('Repasses.tmdl','Codigo_OS'),
    'Receitas_Painel.cod_unidade': dtype('Receitas_Painel.tmdl','cod_unidade'),
    'Despesas_Painel.COD_OS': dtype('Despesas_Painel.tmdl','COD_OS'),
    'Piso_Enfermagem.Codigo_OS': dtype('Piso_Enfermagem.tmdl','Codigo_OS'),
}
if len(set(types.values())) > 1:
    add("P1", "KEY_TYPE_MISMATCH", "Tipos de código OS inconsistentes: " + ", ".join(f"{k}={v}" for k,v in types.items()))

# Regra especial
rep=(TABLES/'Repasses.tmdl').read_text(encoding='utf-8')
if '015/2023-TC' in rep and 'DATE(2023, 12, 1)' in rep:
    add("P2", "HARDCODED_PERIOD_OVERRIDE", "Regra pontual VIVA RIO 015/2023-TC 2023-11 -> 2023-12 detectada.")

# Substituições de mês em Receitas
rec=(TABLES/'Receitas_Painel.tmdl').read_text(encoding='utf-8')
repl=len(re.findall(r'Table\.ReplaceValue', rec))
if repl >= 5:
    add("P2", "MONTH_TEXT_REPLACEMENTS", f"Receitas_Painel normaliza ref_mes com {repl} ReplaceValue encadeados.")

print("Auditoria estrutural do modelo semântico")
print("="*32)
for sev,code,msg in sorted(findings):
    print(f"[{sev}] {code}: {msg}")
print(f"\nFindings: {len(findings)}")
