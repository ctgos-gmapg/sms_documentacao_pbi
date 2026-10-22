# PBI - Piso de Enfermagem

Repositório técnico do painel **Piso_Enfermagem**.

Este repositório documenta o sistema **como ele está implementado hoje (AS-IS)**, com foco em engenharia de dados: origem, ingestão, transformação, chaves, granularidade, relacionamentos, qualidade, atualização e pontos de falha.

## 1. Resumo executivo

A documentação detalhada das conexões e do fluxo de ingestão está em [engenharia_dados/](./engenharia_dados/).

O Power BI está exercendo quatro responsabilidades ao mesmo tempo:

1. **ingestão** de Google Sheets, Excel e PostgreSQL;
2. **transformação** em Power Query;
3. **normalização/dados mestres** de Organização Social e contrato em DAX;
4. **camada semântica** consumida pelo relatório.

Isso funciona, mas aumenta o acoplamento do relatório às fontes e faz com que regras estruturais de dados fiquem dentro do modelo semântico.

### Modelo Relacional

```mermaid
flowchart LR
    GS[Google Sheets / CSV] --> PQ1[Power Query\nRepasses]
    XL1[Excel local\nreceitas_painel.xlsx] --> PQ2[Power Query\nReceitas_Painel]
    XL2[Excel local\ndespesas_painel.xlsx] --> PQ3[Power Query\nDespesas_Painel]
    PG[(PostgreSQL\npublic.rh_pisoenfermagem)] --> PQ4[Power Query\nPiso_Enfermagem]

    PQ1 --> F1[Repasses]
    PQ2 --> F2[Receitas_Painel]
    PQ3 --> F3[Despesas_Painel]
    PQ4 --> F4[Piso_Enfermagem]

    F1 --> DI[dim_instituição]
    F1 --> DC[dim_contrato]
    F2 --> DC
    F3 --> DC
    F4 --> DC

    F1 --> DD[dim_data]
    F2 --> DD
    F3 --> DD
    F4 --> DD

    DI --> SM[Modelo semântico]
    DC --> SM
    DD --> SM
    F1 --> SM
    F2 --> SM
    F3 --> SM
    F4 --> SM
```

## 2. Modelo de dados

O núcleo do modelo é composto por quatro conjuntos transacionais e três dimensões compartilhadas.

| Objeto | Papel | Origem | Grain observado | Chaves de integração |
|---|---|---|---|---|
| `Repasses` | fato de repasses | Google Sheets CSV | registro de repasse | `Codigo_OS`, `Chave_Contrato`, `Ano_Mes_Ref` |
| `Receitas_Painel` | fato de receitas | Excel | item/registro de receita | `cod_unidade`, `Chave_Contrato`, `Ano_Mes_Ref` |
| `Despesas_Painel` | fato de despesas | Excel | documento/registro de despesa | `COD_OS`, `Chave_Contrato`, `Ano_Mes_Ref` |
| `Piso_Enfermagem` | fato de piso de enfermagem | PostgreSQL | registro de profissional/competência da tabela de origem | `Codigo_OS`, `Chave_Contrato`, `rfr_id_referencia` |
| `dim_instituição` | dimensão de OS | DAX calculado | 1 linha por combinação oriunda de `Repasses` | `Codigo_Os` |
| `dim_contrato` | dimensão de contrato | DAX calculado | 1 linha por `Codigo_OS|Contrato` | `Chave_Contrato` |
| `dim_data` | calendário | DAX calculado | 1 linha por dia | `Data` |


## 3. Relacionamentos 

Todos os relacionamentos de negócio presentes no TMDL são do lado fato para dimensão; não há relacionamento fato-fato explícito.

```mermaid
erDiagram
    dim_instituicao ||--o{ Repasses : Codigo_OS
    dim_instituicao ||--o{ Receitas_Painel : cod_unidade
    dim_instituicao ||--o{ Despesas_Painel : COD_OS
    dim_instituicao ||--o{ Piso_Enfermagem : Codigo_OS

    dim_contrato ||--o{ Repasses : Chave_Contrato
    dim_contrato ||--o{ Receitas_Painel : Chave_Contrato
    dim_contrato ||--o{ Despesas_Painel : Chave_Contrato
    dim_contrato ||--o{ Piso_Enfermagem : Chave_Contrato

    dim_data ||--o{ Repasses : Ano_Mes_Ref
    dim_data ||--o{ Receitas_Painel : Ano_Mes_Ref
    dim_data ||--o{ Despesas_Painel : Ano_Mes_Ref
    dim_data ||--o{ Piso_Enfermagem : rfr_id_referencia
```

O modelo possui ainda relacionamentos automáticos com `LocalDateTable_*` para campos de data. Eles são artefatos do **data/hora automática** do Power BI e não fazem parte da modelagem dimensional desejada.
