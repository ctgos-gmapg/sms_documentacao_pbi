# Relacionamentos do modelo Power BI

## Visão geral

O modelo segue uma organização de dimensões e fatos:

- **Fatos:** `Repasses`, `Receitas_Painel`, `Despesas_Painel` e `Piso_Enfermagem`.
- **Dimensões:** `dim_instituição`, `dim_contrato` e `dim_data`.
- **Auxiliar:** `Medida`, sem relação de negócio com as demais tabelas.

As dimensões ficam no lado `1` e as tabelas de fatos no lado `N`. Um registro de dimensão pode filtrar vários registros de fato. Na imagem do Power BI, isso aparece como `1` nas dimensões e `*` nas tabelas transacionais.

## Relação com `dim_instituição`

| Tabela de fato | Coluna na fato | Coluna na dimensão | Finalidade |
|---|---|---|---|
| `Repasses` | `Codigo_OS` | `dim_instituição[Codigo_Os]` | Identifica a organização social do repasse. |
| `Receitas_Painel` | `cod_unidade` | `dim_instituição[Codigo_Os]` | Relaciona a unidade da receita à organização social. |
| `Despesas_Painel` | `COD_OS` | `dim_instituição[Codigo_Os]` | Relaciona a despesa à organização social. |
| `Piso_Enfermagem` | `Codigo_OS` | `dim_instituição[Codigo_Os]` | Relaciona os profissionais e valores à organização social. |

Essa dimensão permite filtrar as quatro fontes por organização social. Ela é atualmente derivada somente de `Repasses`; uma organização que apareça apenas em outra fonte pode não estar disponível para filtragem.

## Relação com `dim_contrato`

| Tabela de fato | Coluna na fato | Coluna na dimensão | Finalidade |
|---|---|---|---|
| `Repasses` | `Chave_Contrato` | `dim_contrato[Chave_Contrato]` | Relaciona o repasse ao contrato. |
| `Receitas_Painel` | `Chave_Contrato` | `dim_contrato[Chave_Contrato]` | Relaciona a receita ao contrato. |
| `Despesas_Painel` | `Chave_Contrato` | `dim_contrato[Chave_Contrato]` | Relaciona a despesa ao contrato. |
| `Piso_Enfermagem` | `Chave_Contrato` | `dim_contrato[Chave_Contrato]` | Relaciona o registro de enfermagem ao contrato. |

`Chave_Contrato` combina o código da organização social e o instrumento do contrato. A dimensão é construída pela união das chaves encontradas nas quatro tabelas.

## Relação com `dim_data`

| Tabela de fato | Coluna na fato | Coluna na dimensão | Finalidade |
|---|---|---|---|
| `Repasses` | `Ano_Mes_Ref` | `dim_data[Data]` | Análise mensal dos repasses. |
| `Receitas_Painel` | `Ano_Mes_Ref` | `dim_data[Data]` | Análise mensal das receitas. |
| `Despesas_Painel` | `Ano_Mes_Ref` | `dim_data[Data]` | Análise mensal das despesas. |
| `Piso_Enfermagem` | `rfr_id_referencia` | `dim_data[Data]` | Análise temporal dos registros de piso. |

`dim_data` é calculada a partir do menor e do maior período encontrados nas quatro fontes. Ela fornece ano, mês, número do mês e o rótulo `Ano_Mes`.

## Relacionamentos automáticos de data

O modelo também possui relações automáticas com tabelas `LocalDateTable_*` para campos de data de `Repasses` e `Despesas_Painel`, como `DATA DE PAGAMENTO`, `DATA DEVOLUÇÃO PROCESSO SUBSECRETARIA`, `Data_Emissao`, `Data_Vencimento`, `Data_Pagamento` e `Data_Apuracao`.

Essas tabelas são criadas pelo recurso **Data/hora automática** do Power BI. Não representam novas fontes e não devem ser confundidas com `dim_data`, que é o calendário oficial. A recomendação é desativar esse recurso e utilizar somente `dim_data`.

## Pontos de atenção

- `Despesas_Painel[COD_OS]` está documentada como texto, enquanto `dim_instituição[Codigo_Os]` é numérica; essa diferença pode causar falhas ou valores sem correspondência.
- A direção esperada do filtro é da dimensão para a fato.
- Chaves nulas, código `0` ou contratos com formatação diferente podem gerar registros sem correspondência.
- `Ano_Mes_Ref` precisa representar uma data válida, normalmente o primeiro dia do mês.
