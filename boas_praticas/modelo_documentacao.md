# Padrão de Documentação dos Projetos Power BI

Este documento define a estrutura recomendada para documentação dos projetos Power BI armazenados neste repositório.

A documentação deve ser construída a partir dos arquivos exportados em formato PBIP, utilizando o modelo semântico, relacionamentos, consultas, tabelas, medidas e demais artefatos do projeto como fonte técnica.

O objetivo é complementar os arquivos do Power BI com informações de contexto, regras de negócio, fluxo de dados e pontos importantes para manutenção.

---

## Estrutura esperada

Cada painel deve possuir uma pasta própria dentro de:

```text
paineis/
```

Exemplo:

```text
paineis/
└── nome_do_painel_pbi/
```
Deve ter sempre _pbi no final, com o objetivo de indicar que é um arquivo Power BI.

A estrutura recomendada é:

```text
nome_do_painel/
├── docs/
├── powerbi/
├── scripts/
└── README.md
```

---

# `docs/`

A pasta `docs/` concentra toda a documentação funcional e técnica do projeto.

A documentação pode ser dividida em grupos de acordo com o conteúdo.

---

## `docs/dicionario/`

Contém a documentação relacionada ao entendimento dos dados e do modelo.

Estrutura recomendada:

```text
docs/
└── dicionario/
    ├── dicionario_de_dados.md
    ├── 01_contexto_do_sistema.md
    ├── 02_sistemas_de_origem.md
    ├── 03_modelo_semantico.md
    ├── 04_transformacoes.md
    ├── 05_qualidade_dos_dados.md
    └── 06_pontos_de_atencao.md
```

### `dicionario_de_dados.md`

Deve apresentar as principais tabelas, campos e significados utilizados no modelo.

Não é necessário documentar campos técnicos irrelevantes.

Priorizar:

- campos utilizados nos relatórios;
- chaves;
- datas;
- indicadores;
- status;
- campos calculados;
- campos relevantes para regras de negócio.

---

### `01_contexto_do_sistema.md`

Deve explicar o contexto funcional do painel.

Incluir:

- finalidade do painel;
- problema que ele resolve;
- área responsável;
- público-alvo;
- principais processos acompanhados;
- escopo da solução.

---

### `02_sistemas_de_origem.md`

Deve listar as fontes utilizadas pelo projeto.

Exemplos:

- PostgreSQL;
- APIs;
- Google Sheets;
- Excel;
- sistemas internos;
- arquivos externos.

Sempre que possível, informar:

```text
Sistema:
Tipo da fonte:
Banco:
Schema:
Tabela/View:
Modo de conexão:
Periodicidade:
```

Não devem ser armazenadas senhas, tokens ou credenciais.

---

### `03_modelo_semantico.md`

Deve explicar a estrutura lógica do modelo semântico.

Incluir:

- tabelas fato;
- dimensões;
- tabelas auxiliares;
- principais medidas;
- organização do modelo;
- granularidade das principais tabelas.

O arquivo deve complementar os arquivos `.tmdl` disponíveis no projeto.

---

### `04_transformacoes.md`

Deve registrar tratamentos realizados antes ou durante a carga dos dados.

Exemplos:

- filtros;
- substituições;
- junções;
- normalizações;
- conversões de tipo;
- criação de colunas;
- regras implementadas no Power Query;
- tratamentos em SQL.

Documentar principalmente transformações que alterem o significado do dado.

---

### `05_qualidade_dos_dados.md`

Deve registrar problemas conhecidos relacionados à qualidade dos dados.

Exemplos:

- campos nulos;
- duplicidades;
- inconsistências;
- divergências entre sistemas;
- ausência de padronização;
- registros incompletos;
- limitações da fonte.

---

### `06_pontos_de_atencao.md`

Deve registrar aspectos importantes para manutenção.

Exemplos:

- dependências externas;
- limitações técnicas;
- regras sensíveis;
- tabelas críticas;
- configurações específicas;
- mudanças que podem impactar o relatório.

---

# `docs/engenharia_dados/`

Contém informações técnicas relacionadas ao fluxo e à estrutura dos dados.

Estrutura sugerida:

```text
docs/
└── engenharia_dados/
    ├── conexoes_e_fluxo.md
    └── relacionamentos_do_modelo.md
```

---

### `conexoes_e_fluxo.md`

Deve descrever como os dados percorrem a solução.

Exemplo:

```text
Sistema de origem
       ↓
Banco de dados
       ↓
View SQL
       ↓
Power Query
       ↓
Modelo Semântico
       ↓
Relatório Power BI
```

Quando houver outras integrações:

```text
Google Sheets
       ↓
Apps Script
       ↓
JSON
       ↓
Power BI
```

---

### `relacionamentos_do_modelo.md`

Deve explicar os principais relacionamentos entre as tabelas.

Priorizar:

- relacionamento entre fatos e dimensões;
- cardinalidade;
- direção de filtro;
- relacionamentos inativos;
- relacionamentos especiais;
- tabelas ponte.

Não é necessário reproduzir todos os relacionamentos quando forem autoexplicativos.

---

### `imagens/`

Utilizada para armazenar imagens relacionadas à documentação.

Exemplos:

- diagrama do modelo;
- arquitetura;
- fluxo de dados;
- relacionamento entre sistemas;
- capturas relevantes do Power BI.

---

# `powerbi/`

Contém os arquivos do projeto exportado em formato PBIP.

Exemplo:

```text
powerbi/
└── semantic-model/
    ├── tables/
    ├── database.tmdl
    ├── expressions.tmdl
    ├── model.tmdl
    └── relationships.tmdl
```

Esses arquivos representam a fonte técnica do projeto.

A documentação não deve simplesmente duplicar o conteúdo dos arquivos TMDL.

Deve explicar o contexto e as decisões que não são evidentes ao analisar apenas o código.

---

# `scripts/`

Contém scripts auxiliares relacionados ao projeto.

Exemplos:

```text
scripts/
├── auditar_modelo_semantico.py
├── extrair_medidas.py
├── validar_relacionamentos.py
└── gerar_documentacao.py
```

Os scripts devem possuir nomes que indiquem claramente sua finalidade.

---

# `README.md`

O `README.md` deve ser o ponto de entrada da documentação do painel.

Deve conter uma visão resumida do projeto e apontar para os documentos mais detalhados.

Estrutura recomendada:

```md
# Nome do Painel

## Visão geral

Descrição resumida do painel.

## Estrutura

- `docs/` — documentação funcional e técnica
- `powerbi/` — arquivos do projeto PBIP
- `scripts/` — scripts auxiliares

## Documentação

### Dados

- Contexto do sistema
- Sistemas de origem
- Modelo semântico
- Transformações
- Qualidade dos dados
- Pontos de atenção

### Engenharia de dados

- Conexões e fluxo
- Relacionamentos do modelo
```

---

# Princípio da documentação

Os arquivos *PBIP* devem ser considerados a fonte técnica do projeto.

A documentação deve responder principalmente às perguntas:

- O que este painel faz?
- De onde vêm os dados?
- Como os dados são transformados?
- Como o modelo está organizado?
- Quais regras não são óbvias?
- Quais problemas de qualidade existem?
- Quais pontos precisam de atenção?
- O que outro profissional precisa saber para manter este projeto?

---

# O que evitar

Evitar documentações que apenas repitam informações já disponíveis nos arquivos `.tmdl`.

Por exemplo, não é necessário listar todas as colunas de uma tabela apenas porque elas existem no modelo.

Priorizar informações que agreguem contexto.

---

# Regra geral

A documentação deve funcionar como complemento ao PBIP.

O projeto deve ser compreensível utilizando:

```text
PBIP
+
Documentação
+
Scripts auxiliares
```

O conjunto deve permitir que outro integrante da equipe consiga entender e manter o painel sem depender exclusivamente do desenvolvedor original.