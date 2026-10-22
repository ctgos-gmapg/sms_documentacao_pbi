# Conexões e fluxo de ingestão

## Resumo

O Power BI recebe quatro fontes principais. Cada uma é lida por uma consulta Power Query e materializada em uma tabela do modelo semântico.

| Fonte | Conector no Power Query | Destino no Power BI | Modo | Dependência para atualização |
|---|---|---|---|---|
| Google Sheets publicado | `Web.Contents` + `Csv.Document` | `Repasses` | Import | URL pública acessível por HTTPS |
| Excel de receitas | `Excel.Workbook` + `File.Contents` | `Receitas_Painel` | Import | arquivo local `receitas_painel.xlsx` |
| Excel de despesas | `Excel.Workbook` + `File.Contents` | `Despesas_Painel` | Import | arquivo local `despesas_painel.xlsx` |
| PostgreSQL | `PostgreSQL.Database` | `Piso_Enfermagem` | Import | servidor, porta, banco e gateway acessíveis |

## 1. Google Sheets — Repasses

### Conexão

Arquivo: `powerbi/semantic-model/tables/Repasses.tmdl`.

O Power Query acessa uma planilha Google Sheets publicada como CSV por meio de `Web.Contents`. A consulta usa delimitador vírgula, codificação UTF-8 e exige exatamente 37 colunas.

Características observadas:

- origem externa via HTTPS;
- cabeçalhos promovidos na primeira linha;
- conversão explícita de tipos;
- filtro de linhas sem `INSTRUMENTO`;
- remoção de colunas auxiliares;
- mapeamento posterior de `Codigo_OS`, `Chave_Contrato` e competência em DAX.

### Dependências e riscos

Se a planilha deixar de ser publicada, mudar a URL, alterar os cabeçalhos ou passar a ter quantidade diferente de colunas, a atualização poderá falhar ou produzir dados incorretos.

## 2. Excel — Receitas

### Conexão

Arquivo: `powerbi/semantic-model/tables/Receitas_Painel.tmdl`.

O Power Query usa `Excel.Workbook` sobre o caminho local configurado no modelo e lê a aba `Sheet1`.

O arquivo atualmente referenciado é:

```text
C:\Users\Windows 11\Documents\Dash Piso Amanda\receitas_painel.xlsx
```

Transformações principais:

- promoção dos cabeçalhos;
- conversão de tipos;
- remoção de `Column1`;
- filtro de `budgetAddCustTAValue` diferente de zero;
- conversão de `ref_mes` para texto;
- normalização de meses por substituições encadeadas.

### Dependências e riscos

O caminho é absoluto e depende de uma máquina específica. No Power BI Service, essa origem exige uma estratégia de gateway, sincronização de arquivo ou substituição por uma localização compartilhada e parametrizada.

## 3. Excel — Despesas

### Conexão

Arquivo: `powerbi/semantic-model/tables/Despesas_Painel.tmdl`.

O Power Query usa `Excel.Workbook` sobre o caminho local configurado no modelo e lê a aba `Planilha1`.

O arquivo atualmente referenciado é:

```text
C:\Users\Windows 11\Documents\Dash Piso Amanda\despesas_painel.xlsx
```

Transformações principais:

- promoção dos cabeçalhos;
- conversão de tipos;
- remoção de colunas auxiliares;
- extração e padronização do código da OS;
- criação de campos de competência e chaves de integração.

### Dependências e riscos

Assim como o arquivo de receitas, o caminho é absoluto e local. A atualização falha quando o arquivo não existe no computador que executa o refresh ou quando a aba `Planilha1` é renomeada.

## 4. PostgreSQL — Piso de Enfermagem

### Conexão

Arquivo: `powerbi/semantic-model/tables/Piso_Enfermagem.tmdl`.

Parâmetros identificados no modelo:

```text
Servidor: 10.1.72.202
Porta: 9203
Banco: ctgos
Schema: public
Tabela: rh_pisoenfermagem
```

No Power Query, a tabela é obtida por:

```m
PostgreSQL.Database("10.1.72.202:9203", "ctgos")
```

Depois da leitura, o modelo normaliza o nome da organização social (`VIVA RIO` para `VIVARIO`) e carrega os campos profissionais, financeiros, contratuais e de referência.

### Dependências e riscos

É necessário acesso de rede ao servidor interno, autenticação válida, permissão de leitura no banco `ctgos` e configuração de gateway quando o refresh ocorrer no Power BI Service. A indisponibilidade do servidor ou da tabela `public.rh_pisoenfermagem` interrompe a atualização dessa fonte.

