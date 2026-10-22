## Pontos de Atenção

### P1 — Excel com caminho absoluto

`Receitas_Painel` e `Despesas_Painel` usam `File.Contents()` apontando para `C:\Users\Windows 11\Documents\...`.

Impacto: refresh não portátil e dependência do filesystem de uma máquina específica.

### P1 — Master data de OS dentro de DAX

`Codigo_OS` é derivado por cadeias de `IF` em `Repasses` e `Piso_Enfermagem`. Valores não mapeados recebem `0`.

Impacto: novas OS podem entrar silenciosamente como `0`, contaminando agregações e relacionamentos.

### P1 — `dim_instituição` depende somente de `Repasses`

A dimensão é construída a partir de `Repasses`, mas é usada para filtrar `Repasses`, `Receitas_Painel`, `Despesas_Painel` e `Piso_Enfermagem`.

Impacto: uma OS existente apenas nas outras fontes não entra na dimensão e fica órfã no modelo.

### P1 — Tipo inconsistente para código da OS

`Repasses[Codigo_OS]`, `Receitas_Painel[cod_unidade]` e `Piso_Enfermagem[Codigo_OS]` são numéricos. `Despesas_Painel[COD_OS]` é texto extraído de `Nome_Os`.

Impacto: coerção implícita, risco de falha de relacionamento e baixa previsibilidade em novas cargas.

### P2 — Regra operacional hardcoded em competência

Há uma exceção explícita para `VIVA RIO`, contrato `015/2023-TC`, pagamento em novembro/2023, movendo a competência para dezembro/2023. A mesma exceção interfere em `ID` e `Ano_Mes_Ref`.

Impacto: regra de negócio sem tabela de parametrização e difícil de auditar.

### P2 — Transformação de mês frágil em receitas

`ref_mes` é normalizado por uma sequência de `Table.ReplaceValue`, incluindo correções posteriores (`0102 -> 12`, `010 -> 10`, `101 -> 11`).

Impacto: lógica dependente de substituição textual, suscetível a efeitos colaterais.

### P2 — Consultas de erro persistidas no modelo

`expressions.tmdl` contém múltiplas consultas `Erros em Repasses*`, criadas em investigações sucessivas de incompatibilidade de tipo.

Impacto: ruído operacional, dificuldade de distinguir monitoramento oficial de artefato de troubleshooting.
