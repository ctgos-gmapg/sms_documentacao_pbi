# Modelo semântico

## Classificação

O modelo segue parcialmente um star schema, mas as dimensões são derivadas dentro do próprio semantic model e existem chaves de negócio concatenadas.

### Fatos / conjuntos transacionais

#### `Repasses`

Valor financeiro principal: `VALOR`.

Integração:

- OS: `Codigo_OS`;
- contrato: `Chave_Contrato`;
- tempo: `Ano_Mes_Ref`;
- chave composta adicional: `ID`.

#### `Receitas_Painel`

Valor de origem: `valor` e diversos campos de orçamento/receita, incluindo `budgetAddCustTAValue` e `totalValue`.

Integração:

- OS: `cod_unidade`;
- contrato: `Chave_Contrato`;
- tempo: `Ano_Mes_Ref`;
- chave composta adicional: `ID`.

#### `Despesas_Painel`

Valores principais: `Valor_Documento`, `Valor_Pago`.

Integração:

- OS: `COD_OS`;
- contrato: `Chave_Contrato`;
- tempo: `Ano_Mes_Ref`;
- chave composta adicional: `ID`.

#### `Piso_Enfermagem`

A origem possui componentes financeiros de piso, incluindo `pe_complemento_mensal`, encargos e vantagens.

Integração:

- OS: `Codigo_OS`;
- contrato: `Chave_Contrato`;
- tempo: `rfr_id_referencia`;
- chave composta adicional: `ID`.

## Dimensões

### `dim_instituição`

Implementação atual:

```DAX
DISTINCT(
    SELECTCOLUMNS(
        Repasses,
        "Nome_Os", Repasses[FAVORECIDO],
        "Codigo_Os", Repasses[Codigo_OS]
    )
)
```

Problema de modelagem: a dimensão compartilhada é abastecida por apenas uma das quatro fontes que ela filtra.

Também existe possibilidade de mais de um `Nome_Os` para o mesmo `Codigo_Os`, porque o `DISTINCT` opera sobre o par `(Nome_Os, Codigo_Os)`, não sobre a chave isolada. Se isso ocorrer, `Codigo_Os` deixa de ser único do lado dimensão.

### `dim_contrato`

É calculada pela união distinta de `Chave_Contrato` das quatro tabelas.

Formato da chave:

```text
<Codigo_OS>|<Contrato>
```

A dimensão decompõe a string para reconstruir `Codigo_Os`, `Instrumento` e buscar `Nome_Os` na `dim_instituição`.

Esse desenho acopla a dimensão ao formato textual da chave. O caractere `|` passa a ser parte do contrato técnico.

### `dim_data`

É gerada do menor ao maior período encontrado nas quatro fontes e expandida para o primeiro e último dia dos respectivos anos.

A relação de competência usa o primeiro dia do mês nas tabelas de fato (`Ano_Mes_Ref`). A dimensão, porém, é diária. Portanto, para essas relações mensais, apenas as linhas de dia 1 participam diretamente da correspondência fato-dimensão.

## Relacionamentos de negócio

| Fato | Dimensão | Chave no fato | Chave na dimensão |
|---|---|---|---|
| Repasses | dim_instituição | `Codigo_OS` | `Codigo_Os` |
| Receitas_Painel | dim_instituição | `cod_unidade` | `Codigo_Os` |
| Despesas_Painel | dim_instituição | `COD_OS` | `Codigo_Os` |
| Piso_Enfermagem | dim_instituição | `Codigo_OS` | `Codigo_Os` |
| Repasses | dim_contrato | `Chave_Contrato` | `Chave_Contrato` |
| Receitas_Painel | dim_contrato | `Chave_Contrato` | `Chave_Contrato` |
| Despesas_Painel | dim_contrato | `Chave_Contrato` | `Chave_Contrato` |
| Piso_Enfermagem | dim_contrato | `Chave_Contrato` | `Chave_Contrato` |
| Repasses | dim_data | `Ano_Mes_Ref` | `Data` |
| Receitas_Painel | dim_data | `Ano_Mes_Ref` | `Data` |
| Despesas_Painel | dim_data | `Ano_Mes_Ref` | `Data` |
| Piso_Enfermagem | dim_data | `rfr_id_referencia` | `Data` |

## Medidas

O TMDL possui uma medida explícita:

```DAX
Total Prestação de Contas = SUM(Despesas_Painel[Valor_Pago])
```

A baixa quantidade de measures indica que parte relevante dos cálculos pode estar sendo feita por agregação implícita de colunas nos visuais. Para governança semântica, recomenda-se centralizar KPIs em measures explícitas.
