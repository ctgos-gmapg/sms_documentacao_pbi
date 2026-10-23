# Conexões e fluxo de ingestão

## Resumo

O Power BI recebe quatro fontes principais. Cada uma é lida por uma consulta Power Query e materializada em uma tabela do modelo semântico.

| Fonte | Conector no Power Query | Destino no Power BI | Modo | Dependência para atualização |
|---|---|---|---|---|
| Google Sheets publicado | `Web.Contents` + `Csv.Document` | `Repasses` | Import | URL pública acessível por HTTPS |
| Excel de receitas | `Excel.Workbook` + `File.Contents` | `Receitas_Painel` | Import | arquivo local `receitas_painel.xlsx` |
| Excel de despesas | `Excel.Workbook` + `File.Contents` | `Despesas_Painel` | Import | arquivo local `despesas_painel.xlsx` |
| PostgreSQL | `PostgreSQL.Database` | `Piso_Enfermagem` | Import | servidor, porta, banco e gateway acessíveis |
