# Identidade Visual — Prefeitura do Rio

Este documento apresenta as diretrizes visuais adotadas nos dashboards e produtos de Business Intelligence, tendo como referência a identidade visual institucional da Prefeitura da Cidade do Rio de Janeiro.

O objetivo é manter consistência entre os painéis, garantir legibilidade e aproximar os produtos de dados da identidade institucional.

---

## Paleta institucional

### Azul principal

Cor principal da identidade visual.

```text
HEX: #13335A
RGB: 19, 51, 90
```

**Aplicações recomendadas:**

- cabeçalhos;
- títulos principais;
- menus laterais;
- elementos de navegação;
- botões;
- destaques institucionais;
- fundos de capa.

---

### Azul intermediário

```text
HEX: #2A688F
RGB: 42, 104, 143
```

**Aplicações recomendadas:**

- gráficos;
- elementos secundários;
- barras;
- ícones;
- destaques;
- componentes de apoio.

---

### Azul claro

```text
HEX: #42B9EB
RGB: 66, 185, 235
```

**Aplicações recomendadas:**

- destaques;
- indicadores;
- elementos selecionados;
- estados ativos;
- gráficos;
- pontos de atenção visual.

---

### Cinza institucional

```text
HEX: #ECEDED
RGB: 236, 237, 237
```

**Aplicações recomendadas:**

- fundos secundários;
- separadores;
- áreas de agrupamento;
- componentes desabilitados;
- contraste leve entre seções.

---

### Branco

```text
HEX: #FFFFFF
RGB: 255, 255, 255
```

Utilizar como cor predominante de fundo dos dashboards.

O uso de fundo branco contribui para:

- melhor leitura;
- redução de poluição visual;
- maior destaque dos indicadores;
- melhor contraste com as cores institucionais.

---

## Paleta recomendada para Power BI

Para manter consistência entre dashboards, utilizar preferencialmente a seguinte ordem de cores:

| Uso | Cor | HEX |
|---|---|---|
| Primária | Azul institucional | `#13335A` |
| Secundária | Azul intermediário | `#2A688F` |
| Destaque | Azul claro | `#42B9EB` |
| Fundo secundário | Cinza claro | `#ECEDED` |
| Fundo principal | Branco | `#FFFFFF` |

---

## Degradê institucional

Quando necessário, pode ser utilizado o degradê:

```text
#2A688F → #42B9EB
```

Exemplo conceitual:

```text
Azul intermediário                     Azul claro
#2A688F  ────────────────────────────  #42B9EB
```

O degradê pode ser utilizado principalmente em:

- capas;
- cabeçalhos;
- elementos gráficos institucionais;
- áreas de destaque.

Evitar o uso excessivo do degradê dentro das páginas analíticas.

---

# Tipografia

A identidade institucional utiliza a família:

```text
Cera Pro
```

Com as seguintes aplicações:

### Cera Pro Black

Utilizar preferencialmente em:

- títulos principais;
- grandes indicadores;
- chamadas de destaque.

---

### Cera Pro Medium

Utilizar em:

- subtítulos;
- títulos de cards;
- títulos de gráficos;
- botões;
- menus.

---

### Cera Pro Regular

Utilizar em:

- textos explicativos;
- descrições;
- tooltips;
- tabelas;
- textos auxiliares.

---

## Tipografia no Power BI

Quando a fonte institucional não estiver disponível ou não for adequada ao ambiente de publicação, utilizar uma fonte de sistema com boa legibilidade.

Priorizar:

```text
DIN ou MONTSERRAT
```

Sugestão:

| Elemento | Peso |
|---|---|
| Título da página | Semibold / Bold |
| Indicador | Semibold / Bold |
| Título de card | Semibold |
| Texto | Regular |
| Texto auxiliar | Regular |

---

# Hierarquia visual

Os dashboards devem apresentar claramente a seguinte hierarquia:

```text
Título da página

Indicadores principais

Filtros e Ajuda (modelo pop-up)

Visualizações principais

Visualizações secundárias

Detalhamento
```

Evitar que todos os elementos tenham o mesmo peso visual.

---

# Estrutura recomendada

Uma página típica pode seguir:

```text
┌─────────────────────────────────────────────────────────────┐
│ TÍTULO DA PÁGINA                                            │
├───────────────┬───────────────┬───────────────┬─────────────┤
│ Indicador 01  │ Indicador 02  │ Indicador 03  │ Indicador 04│
├───────────────┴───────────────┴───────────────┴─────────────┤
│                                                             │
│                    Visual principal                         │
│                                                             │
├─────────────────────────────┬───────────────────────────────┤
│ Visual secundário           │ Visual secundário             │
│                             │                               │
└─────────────────────────────┴───────────────────────────────┘
```

---

# Cards

Utilizar cards para destacar indicadores importantes.

## Recomendações

- fundo branco;
- bordas discretas;
- cantos levemente arredondados;
- espaçamento interno consistente;
- indicador em destaque;
- título menor que o valor;
- evitar excesso de sombras.

Exemplo:

```text
┌──────────────────────────┐
│ Total Repassado          │
│                          │
│ R$ 12,4 mi               │
│                          │
│ ↑ 8,4%                   │
└──────────────────────────┘
```

---

# Cantos

Manter consistência entre os componentes.

Sugestão:

```text
Cards principais:        8 px
Cards secundários:       6–8 px
Botões:                  6–8 px
Filtros:                 6–8 px
```

Evitar misturar muitos níveis diferentes de arredondamento.

---

# Espaçamento

Utilizar múltiplos de `4 px`.

Escala recomendada:

```text
4 px
8 px
12 px
16 px
24 px
32 px
```

Sugestões:

```text
Entre elementos internos:    8–12 px
Entre cards:                  12–16 px
Entre seções:                 24–32 px
Margem da página:             24–32 px
```

---

# Sidebar

Quando utilizada, a barra lateral deve possuir função clara de navegação.

Recomenda-se:

```text
Fundo: #13335A
Texto: #FFFFFF
Ícones: #FFFFFF
Item ativo: #42B9EB
```

Estrutura sugerida:

```text
┌─────────────────┐
│                 │
│ LOGO            │
│                 │
│ ▣ Visão Geral   │
│ ▢ Repasses      │
│ ▢ Contratos     │
│ ▢ Detalhamento  │
│                 │
│  Filtro         │
│  Ajuda          │
└─────────────────┘
```

---

# Gráficos

Evitar utilizar uma cor diferente para cada elemento sem necessidade.

Para gráficos da mesma categoria, priorizar variações da paleta institucional.

Exemplo:

```text
#13335A
#2A688F
#42B9EB
```

Para comparações, a cor mais importante deve possuir maior destaque.

---

## Cor neutra

Categorias secundárias podem utilizar tons neutros.

Sugestões:

```text
#6B7280
#9CA3AF
#D1D5DB
#ECEDED
```

---

# Cores semânticas

As cores institucionais não devem ser utilizadas para substituir cores de significado universal quando isso prejudicar a compreensão.

Sugestão:

### Sucesso

```text
#2E7D32
```

### Atenção

```text
#F9A825
```

### Erro / crítico

```text
#C62828
```

### Informação

```text
#2A688F
```

Utilizar essas cores apenas quando houver significado associado.

Exemplo:

```text
Pago        → Verde
Pendente    → Amarelo
Atrasado    → Vermelho
```

Não utilizar vermelho apenas como decoração.

---

# Fundos

Priorizar:

```text
#FFFFFF
```

ou

```text
#ECEDED
```

Fundos escuros devem ser utilizados principalmente em:

- capas;
- cabeçalhos;
- menus;
- áreas institucionais.

Evitar páginas analíticas completamente escuras, salvo quando houver justificativa específica de projeto.

---

# Contraste

Garantir contraste adequado entre texto e fundo.

Exemplos recomendados:

```text
#13335A sobre #FFFFFF
#FFFFFF sobre #13335A
#FFFFFF sobre #2A688F
```

Evitar:

```text
#42B9EB sobre #FFFFFF
```

para textos pequenos, devido ao contraste reduzido.

---

# Logotipo

A marca institucional deve ser utilizada respeitando:

- proporções originais;
- espaçamento de segurança;
- cores oficiais;
- versões previstas no manual institucional.

Não:

- distorcer;
- inclinar;
- alterar proporções;
- modificar cores;
- adicionar contorno;
- separar elementos da marca;
- aplicar sobre fundos que prejudiquem sua leitura.

---

# Fotografias

Quando utilizadas, priorizar imagens:

- naturais;
- contextualizadas;
- relacionadas ao serviço público;
- sem excesso de tratamento;
- com boa qualidade visual.

Evitar fotografias meramente decorativas dentro de páginas analíticas.

---

# Padrão dos dashboards

Os dashboards devem transmitir:

**clareza, objetividade, consistência e institucionalidade.**

Priorizar:

- espaço em branco;
- baixa poluição visual;
- hierarquia clara;
- poucos elementos por página;
- alinhamentos consistentes;
- paleta reduzida;
- destaque para os dados;
- navegação simples.

---

# Resumo rápido

```text
Azul principal
#13335A

Azul intermediário
#2A688F

Azul claro
#42B9EB

Cinza institucional
#ECEDED

Branco
#FFFFFF
```

Degradê:

```text
#2A688F → #42B9EB
```

Tipografia institucional:

```text
Cera Pro
```

Tipografia recomendada para Power BI em títulos:

```text
DIN
```

Tipografia recomendada para Power BI em valores:

```text
DIN Light
```
---

## Referência

As cores, tipografia e orientações institucionais apresentadas neste documento têm como referência o Manual de Marca da Prefeitura do Rio.

As recomendações específicas para dashboards complementam a identidade institucional com boas práticas de UX/UI e visualização de dados.