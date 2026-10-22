# Sistemas de origem e conectividade

## Matriz de fontes

| Dataset | Tecnologia | Endpoint físico | Modo | Transformação de entrada | Risco operacional |
|---|---|---|---|---|---|
| `Repasses` | Google Sheets publicado como CSV | `Web.Contents(...)` | Import | promoção de cabeçalho, tipagem, filtro e remoção de colunas | schema externo sem contrato |
| `Receitas_Painel` | Excel | caminho absoluto local | Import | tipagem, filtro, normalização de mês | não portátil |
| `Despesas_Painel` | Excel | caminho absoluto local | Import | tipagem, remoção de colunas, extração de código da OS | não portátil |
| `Piso_Enfermagem` | PostgreSQL | servidor interno / DB `ctgos` | Import | leitura de `public.rh_pisoenfermagem` + normalização de nome | requer conectividade interna/gateway |

## Repasses

A consulta usa `Csv.Document(Web.Contents(...))` com `Columns=37` e UTF-8.

### Contrato técnico implícito

- exatamente 37 colunas no CSV;
- cabeçalhos compatíveis com a lista passada para `Table.TransformColumnTypes`;
- `INSTRUMENTO` não nulo para registros mantidos;
- campos de data parseáveis pelo locale/contexto do Power Query.

A indicação fixa de `Columns=37` torna a ingestão sensível a alteração estrutural do Google Sheets.

## Receitas_Painel

Fonte atual:

```text
C:\Users\Windows 11\Documents\Dash Piso Amanda\receitas_painel.xlsx
```

Planilha consumida: `Sheet1`.

O filtro de entrada mantém somente linhas onde `budgetAddCustTAValue <> 0`. Portanto, o modelo não representa todo o conteúdo do arquivo; representa um subconjunto de receitas condicionado a esse campo.

## Despesas_Painel

Fonte atual:

```text
C:\Users\Windows 11\Documents\Dash Piso Amanda\despesas_painel.xlsx
```

Planilha consumida: `Planilha1`.

`COD_OS` é derivado com:

```text
Text.BeforeDelimiter([Nome_Os], " ")
```

Logo, o modelo assume que `Nome_Os` começa pelo código institucional seguido de espaço.

## Piso_Enfermagem

Origem lógica:

```text
database: ctgos
schema: public
table: rh_pisoenfermagem
```

A consulta substitui `VIVA RIO` por `VIVARIO` na coluna `pe_organizacao_social` antes do carregamento no modelo.

## Atualização

O modelo é `Import`. Portanto, disponibilidade do relatório não depende de consulta online às fontes durante interação, mas a atualização do dataset depende simultaneamente de:

- acesso HTTP ao Google Sheets publicado;
- acesso aos dois arquivos Excel;
- acesso ao PostgreSQL interno.

Qualquer pipeline de publicação/gateway precisa resolver essas três classes de conectividade.
