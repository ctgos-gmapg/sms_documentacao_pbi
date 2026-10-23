# Contexto do sistema

## Responsabilidades implementadas no Power BI

| Responsabilidade | Implementação atual | Observação |
|---|---|---|
| extração | M / Power Query | quatro fontes heterogêneas |
| conversão de esquema | M / `Table.TransformColumnTypes` | forte dependência do esquema da origem |
| filtragem | M | ex.: receitas filtra `budgetAddCustTAValue <> 0` |
| padronização | M + DAX | nomes de OS e mês |
| surrogate/business key | DAX | concatenação de código + contrato |
| dados mestres | DAX | mapeamentos de OS e dimensões calculadas |
| calendário | DAX | `dim_data` + LocalDateTables automáticas |
| métrica | DAX | `Total Prestação de Contas` |



O desenho atual é um **modelo semântico com ETL embutido**. Não há evidência no projeto de uma camada de modelo medalhão staging/bronze/silver externa ao Power BI para estas quatro fontes.

Esse ponto é importante: mudanças de origem, mappings e regras de qualidade exigem publicação do dataset, não apenas atualização de uma tabela upstream.
