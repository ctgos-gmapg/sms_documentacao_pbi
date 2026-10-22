![Rio Prefeitura Saúde](design/logo/RIOPREFEITURA%20Saúde%20vertical%20monocromática%20azul.png)

# Documentação Power BI — SMS

Repositório destinado à centralização da documentação técnica e funcional dos painéis desenvolvidos em Power BI, incluindo informações sobre fontes de dados, modelo semântico, regras de negócio, configurações, conexões, padrões de documentação e identidade visual.

O objetivo é facilitar a manutenção, o entendimento das soluções existentes, a padronização dos projetos e a continuidade do desenvolvimento pela equipe.

---

## Estrutura do repositório

```text
sms_documentacao_pbi/
│
├── boas_praticas/
│   └── modelo_documentacao.md
│
├── configuracoes/
│   ├── conexoes/
│   ├── gateway/
│   └── pbi_service/
│
├── design/
│   ├── logo/
│   └── manual_marca/
│
├── paineis/
│   ├── demandas_gmapg_pbi/
│   └── piso_enfermagem_pbi/
│
└── README.md
```

---

## `boas_praticas/`

Centraliza orientações e padrões recomendados para organização e documentação dos projetos Power BI.

Atualmente, esta pasta contém o arquivo:

```text
modelo_documentacao.md
```

Esse documento define como a documentação de cada painel deve ser estruturada, considerando que os projetos são mantidos em formato PBIP.

A documentação deve complementar os arquivos técnicos do projeto, registrando principalmente informações que não são facilmente identificadas apenas pela análise do modelo semântico.

Entre os principais pontos esperados estão:

- contexto do sistema;
- sistemas e fontes de origem;
- modelo semântico;
- transformações realizadas;
- qualidade dos dados;
- conexões e fluxo de dados;
- relacionamentos;
- pontos de atenção;
- regras e decisões importantes para manutenção.

---

## `configuracoes/`

Contém documentações e procedimentos compartilhados entre diferentes projetos Power BI.

Essa pasta deve concentrar configurações que não pertencem exclusivamente a um único painel.

### `conexoes/`

Documentação relacionada às diferentes formas de conexão utilizadas pelos projetos.

Exemplos:

- PostgreSQL;
- APIs REST;
- Google Sheets;
- Google Apps Script;
- arquivos externos;
- outras fontes de dados.

Podem ser incluídos procedimentos de configuração, exemplos de conexão e particularidades necessárias para utilização no Power BI.

### `gateway/`

Documentação relacionada ao Power BI Gateway.

Exemplos:

- instalação;
- configuração;
- criação de fontes de dados;
- associação com conjuntos de dados;
- configuração de credenciais;
- solução de problemas comuns.

### `pbi_service/`

Documentação relacionada ao Power BI Service.

Exemplos:

- publicação;
- workspaces;
- atualização agendada;
- credenciais;
- permissões;
- configuração de datasets/modelos semânticos;
- parametrizações;
- procedimentos de manutenção.

Configurações específicas de apenas um painel devem permanecer documentadas dentro da pasta correspondente ao projeto.

---

## `design/`

Centraliza os recursos relacionados à identidade visual utilizada nos dashboards.

### `logo/`

Contém arquivos oficiais de logotipo utilizados nos projetos.

Sempre que possível, utilizar os arquivos disponibilizados nesta pasta em vez de criar novas versões ou alterar manualmente os elementos da marca.

### `manual_marca/`

Contém materiais de referência relacionados à identidade visual institucional.

Pode incluir:

- manual da marca;
- paleta de cores;
- tipografia;
- orientações de aplicação;
- referências visuais.

Os dashboards devem respeitar a identidade institucional e manter consistência visual entre os diferentes projetos.

---

## `paineis/`

Contém os projetos Power BI e suas respectivas documentações.

Cada painel deve possuir sua própria pasta.

Exemplo:

```text
paineis/
├── demandas_gmapg_pbi/
└── piso_enfermagem_pbi/
```

Cada projeto pode conter:

```text
nome_do_painel_pbi/
├── docs/
├── powerbi/
├── scripts/
└── README.md
```

A estrutura interna pode variar de acordo com a necessidade do projeto, mas deve seguir, sempre que possível, as orientações definidas em:

```text
boas_praticas/modelo_documentacao.md
```

---

## Estrutura recomendada de um painel

Um projeto documentado pode seguir o padrão:

```text
nome_do_painel_pbi/
│
├── docs/
│   ├── dicionario/
│   │   ├── dicionario_de_dados.md
│   │   ├── 01_contexto_do_sistema.md
│   │   ├── 02_sistemas_de_origem.md
│   │   ├── 03_modelo_semantico.md
│   │   ├── 04_transformacoes.md
│   │   ├── 05_qualidade_dos_dados.md
│   │   └── 06_pontos_de_atencao.md
│   │
│   └── engenharia_dados/
│       ├── conexoes_e_fluxo.md
│       ├── relacionamentos_do_modelo.md
│       └── imagens/
│
├── powerbi/
│   └── semantic-model/
│
├── scripts/
│
└── README.md
```

O objetivo não é obrigar todos os projetos a possuir exatamente os mesmos arquivos, mas manter uma estrutura suficientemente padronizada para facilitar a navegação e manutenção.

---

## Projetos documentados

| Painel | Descrição | Documentação |
|---|---|---|
| Demandas GMAPG | Projeto Power BI relacionado ao acompanhamento das demandas GMAPG | [Acessar](paineis/demandas_gmapg_pbi/) |
| Piso da Enfermagem | Projeto Power BI relacionado ao acompanhamento das informações do Piso da Enfermagem | [Acessar](paineis/piso_enfermagem_pbi/) |

> Atualizar esta tabela sempre que um novo painel for incluído no repositório.

---

## Como adicionar um novo painel

Para incluir um novo projeto:

1. Criar uma pasta dentro de `paineis/`.
2. Utilizar nomes em `snake_case`.
3. Utilizar o sufixo `_pbi` para identificar projetos Power BI.
4. Exportar ou organizar o projeto no formato PBIP.
5. Criar a estrutura necessária para documentação.
6. Seguir as orientações disponíveis em `boas_praticas/modelo_documentacao.md`.
7. Criar um `README.md` na raiz do projeto.
8. Atualizar a seção **Projetos documentados** deste README.

Exemplo:

```text
paineis/
└── novo_painel_pbi/
```

---

## Padrão de nomenclatura

Utilizar preferencialmente:

```text
snake_case
```

Para projetos Power BI:

```text
nome_do_painel_pbi
```

Exemplos:

```text
piso_enfermagem_pbi
demandas_gmapg_pbi
prestacao_contas_pbi
controle_repasses_pbi
```

Para arquivos Markdown:

```text
contexto_do_sistema.md
modelo_semantico.md
conexoes_e_fluxo.md
```

Evitar:

```text
Piso Enfermagem
Piso-Enfermagem
pisoEnfermagem
Contexto Do Sistema.md
```

---

## Documentação dos projetos

Os arquivos PBIP devem ser considerados a principal fonte técnica do projeto.

A documentação deve complementar essas informações, registrando principalmente:

- contexto funcional;
- finalidade do painel;
- origem dos dados;
- fluxo das informações;
- regras de negócio;
- transformações relevantes;
- estrutura do modelo;
- problemas de qualidade;
- dependências;
- limitações;
- decisões técnicas;
- pontos importantes para manutenção.

Não é necessário duplicar manualmente informações que já podem ser facilmente identificadas nos arquivos do projeto.

A documentação deve priorizar aquilo que exige contexto para ser compreendido.

---

## Segurança

Este repositório não deve armazenar informações sensíveis, como:

- senhas;
- tokens de API;
- chaves de acesso;
- credenciais de banco de dados;
- arquivos `.env`;
- secrets de aplicações;
- dados pessoais ou restritos sem necessidade.

Quando necessário, a documentação deve apenas indicar onde a credencial está configurada.

Exemplo:

```text
Fonte: PostgreSQL
Servidor: servidor-interno
Banco: base_indicadores
Autenticação: credencial configurada no Power BI Gateway
```

---

## Manutenção da documentação

Sempre que houver uma alteração relevante em um projeto, avaliar se a documentação também precisa ser atualizada.

Mudanças que normalmente devem ser documentadas incluem:

- inclusão ou remoção de fontes de dados;
- alteração de regras de negócio;
- mudanças no modelo semântico;
- novos relacionamentos;
- alterações importantes no processo de transformação;
- mudanças na forma de atualização;
- novas dependências;
- problemas conhecidos ou limitações identificadas.

A documentação deve acompanhar a evolução do projeto.

---

## Objetivo da documentação

A documentação deve permitir que outro integrante da equipe consiga compreender:

**o que o painel faz → de onde vêm os dados → como os dados são tratados → como o modelo está estruturado → quais regras são aplicadas → quais dependências existem → como o projeto pode ser mantido.**

O conjunto formado por:

```text
Projeto PBIP
    +
Documentação
    +
Configurações
    +
Scripts auxiliares
```

deve fornecer contexto suficiente para que o projeto possa ser compreendido e mantido sem depender exclusivamente do desenvolvedor original.