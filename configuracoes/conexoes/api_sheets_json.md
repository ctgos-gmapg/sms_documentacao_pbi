# Criando uma API JSON com Google Apps Script

Este documento descreve como disponibilizar os dados de uma planilha do Google Sheets em formato JSON utilizando Google Apps Script.

A solução pode ser utilizada como fonte de dados para aplicações, integrações e ferramentas como o Power BI.

---

## Visão geral

O fluxo funciona da seguinte forma:

```text
Google Sheets
     ↓
Google Apps Script
     ↓
Web App
     ↓
Endpoint HTTP
     ↓
JSON
     ↓
Power BI / Aplicação
```

O Google Apps Script lê os dados da planilha e disponibiliza essas informações por meio de uma URL pública ou restrita.

Exemplo:

```text
https://script.google.com/macros/s/SEU_ID/exec
```

Ao acessar essa URL, o retorno será semelhante a:

```json
[
  {
    "ID": 1,
    "UNIDADE": "Unidade A",
    "VALOR": 1500.25
  },
  {
    "ID": 2,
    "UNIDADE": "Unidade B",
    "VALOR": 2300.50
  }
]
```

---

# 1. Acessar o Google Apps Script

Abra a planilha que será utilizada como fonte.

No menu superior do Google Sheets, acesse:

```text
Extensões
→ Apps Script
```

Será aberto um projeto do Google Apps Script associado à planilha.

---

# 2. Criar o script

Apague o conteúdo inicial do arquivo `Code.gs` e utilize:

```javascript
function doGet() {

  const planilha = SpreadsheetApp.getActiveSpreadsheet();

  const aba = planilha.getSheetByName("BASE");

  const dados = aba.getDataRange().getValues();

  const cabecalho = dados.shift();

  const resultado = dados.map(linha => {

    const registro = {};

    cabecalho.forEach((coluna, indice) => {
      registro[coluna] = linha[indice];
    });

    return registro;

  });

  return ContentService
    .createTextOutput(JSON.stringify(resultado))
    .setMimeType(ContentService.MimeType.JSON);

}
```

---

# 3. Estrutura esperada da planilha

A primeira linha da planilha deve possuir o nome das colunas.

Exemplo:

| ID | UNIDADE | VALOR |
|---|---|---:|
| 1 | Unidade A | 1500 |
| 2 | Unidade B | 2300 |

O script utilizará o cabeçalho para criar os nomes das propriedades do JSON.

O resultado será:

```json
[
  {
    "ID": 1,
    "UNIDADE": "Unidade A",
    "VALOR": 1500
  },
  {
    "ID": 2,
    "UNIDADE": "Unidade B",
    "VALOR": 2300
  }
]
```

---

# 4. Cabeçalho em outra linha

Nem sempre o cabeçalho está localizado na primeira linha da planilha.

Por exemplo:

```text
Linha 1 → título
Linha 2 → observação
Linha 3 → cabeçalho
Linha 4 → início dos dados
```

Nesse caso, é possível definir a linha inicial manualmente.

Exemplo:

```javascript
function doGet() {

  const planilha = SpreadsheetApp.getActiveSpreadsheet();

  const aba = planilha.getSheetByName("BASE");

  const linhaCabecalho = 3;

  const ultimaLinha = aba.getLastRow();
  const ultimaColuna = aba.getLastColumn();

  const dados = aba
    .getRange(
      linhaCabecalho,
      1,
      ultimaLinha - linhaCabecalho + 1,
      ultimaColuna
    )
    .getValues();

  const cabecalho = dados.shift();

  const resultado = dados.map(linha => {

    const registro = {};

    cabecalho.forEach((coluna, indice) => {
      registro[coluna] = linha[indice];
    });

    return registro;

  });

  return ContentService
    .createTextOutput(JSON.stringify(resultado))
    .setMimeType(ContentService.MimeType.JSON);

}
```

Neste exemplo, a linha `3` é considerada o cabeçalho.

---

# 5. Trabalhando com múltiplas abas

Caso uma mesma planilha possua diferentes bases, pode ser utilizado um parâmetro na URL.

Exemplo:

```text
?aba=base
```

ou:

```text
?aba=publicacao
```

Exemplo de URLs:

```text
https://script.google.com/macros/s/SEU_ID/exec?aba=base
```

```text
https://script.google.com/macros/s/SEU_ID/exec?aba=publicacao
```

---

## Script com múltiplas abas

```javascript
function doGet(e) {

  const planilha = SpreadsheetApp.getActiveSpreadsheet();

  const parametro = e.parameter.aba || "base";

  const configuracoes = {

    base: {
      aba: "BASE 2024 A 2025",
      cabecalho: 1
    },

    publicacao: {
      aba: "PUBLICAÇÃO",
      cabecalho: 2
    }

  };

  const config = configuracoes[parametro];

  if (!config) {

    return ContentService
      .createTextOutput(
        JSON.stringify({
          erro: "Aba inválida"
        })
      )
      .setMimeType(ContentService.MimeType.JSON);

  }

  const aba = planilha.getSheetByName(config.aba);

  const ultimaLinha = aba.getLastRow();
  const ultimaColuna = aba.getLastColumn();

  const dados = aba
    .getRange(
      config.cabecalho,
      1,
      ultimaLinha - config.cabecalho + 1,
      ultimaColuna
    )
    .getValues();

  const cabecalho = dados.shift();

  const resultado = dados.map(linha => {

    const registro = {};

    cabecalho.forEach((coluna, indice) => {
      registro[coluna] = linha[indice];
    });

    return registro;

  });

  return ContentService
    .createTextOutput(JSON.stringify(resultado))
    .setMimeType(ContentService.MimeType.JSON);

}
```

Com essa estrutura, novas abas podem ser adicionadas facilmente:

```javascript
const configuracoes = {

  base: {
    aba: "BASE 2024 A 2025",
    cabecalho: 1
  },

  publicacao: {
    aba: "PUBLICAÇÃO",
    cabecalho: 2
  },

  contratos: {
    aba: "CONTRATOS",
    cabecalho: 1
  }

};
```

---

# 6. Ignorar linhas vazias

É recomendado remover linhas completamente vazias antes de gerar o JSON.

Exemplo:

```javascript
const linhasValidas = dados.filter(linha =>
  linha.some(valor => valor !== "")
);
```

Aplicação:

```javascript
const resultado = dados
  .filter(linha => linha.some(valor => valor !== ""))
  .map(linha => {

    const registro = {};

    cabecalho.forEach((coluna, indice) => {
      registro[coluna] = linha[indice];
    });

    return registro;

  });
```

---

# 7. Tratamento de datas

Datas do Google Sheets são retornadas pelo Apps Script como objetos `Date`.

Para APIs utilizadas pelo Power BI, recomenda-se padronizar essas datas.

Exemplo:

```javascript
function formatarValor(valor) {

  if (valor instanceof Date) {
    return Utilities.formatDate(
      valor,
      Session.getScriptTimeZone(),
      "yyyy-MM-dd"
    );
  }

  return valor;

}
```

Depois, utilize:

```javascript
cabecalho.forEach((coluna, indice) => {
  registro[coluna] = formatarValor(linha[indice]);
});
```

O JSON passa a retornar:

```json
{
  "DATA": "2026-10-22"
}
```

em vez de formatos de data menos previsíveis.

---

# 8. Script recomendado

Uma estrutura mais completa pode ser utilizada como padrão:

```javascript
function doGet(e) {

  try {

    const planilha = SpreadsheetApp.getActiveSpreadsheet();

    const parametro = e.parameter.aba || "base";

    const configuracoes = {

      base: {
        aba: "BASE 2024 A 2025",
        cabecalho: 1
      },

      publicacao: {
        aba: "PUBLICAÇÃO",
        cabecalho: 2
      }

    };

    const config = configuracoes[parametro];

    if (!config) {
      return criarResposta({
        erro: true,
        mensagem: "Parâmetro de aba inválido."
      });
    }

    const aba = planilha.getSheetByName(config.aba);

    if (!aba) {
      return criarResposta({
        erro: true,
        mensagem: "A aba configurada não foi encontrada."
      });
    }

    const ultimaLinha = aba.getLastRow();
    const ultimaColuna = aba.getLastColumn();

    if (ultimaLinha <= config.cabecalho) {
      return criarResposta([]);
    }

    const dados = aba
      .getRange(
        config.cabecalho,
        1,
        ultimaLinha - config.cabecalho + 1,
        ultimaColuna
      )
      .getValues();

    const cabecalho = dados.shift();

    const resultado = dados
      .filter(linha =>
        linha.some(valor => valor !== "")
      )
      .map(linha => {

        const registro = {};

        cabecalho.forEach((coluna, indice) => {

          if (!coluna) {
            return;
          }

          registro[coluna] =
            formatarValor(linha[indice]);

        });

        return registro;

      });

    return criarResposta(resultado);

  } catch (erro) {

    return criarResposta({
      erro: true,
      mensagem: erro.message
    });

  }

}

function formatarValor(valor) {

  if (valor instanceof Date) {

    return Utilities.formatDate(
      valor,
      Session.getScriptTimeZone(),
      "yyyy-MM-dd"
    );

  }

  return valor;

}

function criarResposta(dados) {

  return ContentService
    .createTextOutput(
      JSON.stringify(dados)
    )
    .setMimeType(
      ContentService.MimeType.JSON
    );

}
```

---

# 9. Publicar como Web App

Depois de criar o script:

```text
Implantar
→ Nova implantação
```

Clique em:

```text
Selecionar tipo
→ App da Web
```

Configure:

```text
Executar como:
Eu

Quem pode acessar:
Qualquer pessoa
```

Dependendo da política da organização, as opções disponíveis podem ser diferentes.

Depois clique em:

```text
Implantar
```

O Google solicitará autorização para execução do script.

Ao finalizar, será apresentada uma URL semelhante a:

```text
https://script.google.com/macros/s/XXXXXXXXXXXX/exec
```

Essa será a URL utilizada como endpoint da API.

---

# 10. Testando o endpoint

Abra a URL no navegador:

```text
https://script.google.com/macros/s/SEU_ID/exec
```

Se forem utilizados parâmetros:

```text
https://script.google.com/macros/s/SEU_ID/exec?aba=base
```

O navegador deverá retornar o conteúdo em JSON.

Exemplo:

```json
[
  {
    "UG": "1800",
    "UNIDADE": "SMS",
    "INSTRUMENTO": "0001",
    "VALOR": 12500.50
  }
]
```

---

# 11. Atualizando o script

Após alterar o código, é importante verificar a implantação.

Acesse:

```text
Implantar
→ Gerenciar implantações
```

Selecione a implantação existente e crie uma nova versão.

Não é necessário criar um novo Web App sempre que o código for atualizado.

Preferencialmente mantenha a mesma URL utilizada pelo Power BI.

---

# 12. Consumindo no Power BI

No Power Query:

```powerquery
let
    Fonte =
        Json.Document(
            Web.Contents(
                "https://script.google.com/macros/s/SEU_ID/exec?aba=base"
            )
        )
in
    Fonte
```

Depois, os registros podem ser convertidos para tabela.

Exemplo:

```powerquery
let
    Fonte =
        Json.Document(
            Web.Contents(
                "https://script.google.com/macros/s/SEU_ID/exec?aba=base"
            )
        ),

    Tabela =
        Table.FromRecords(Fonte)

in
    Tabela
```

---

# 13. Boas práticas

## Não utilizar índices fixos desnecessariamente

Preferir:

```javascript
getLastRow()
getLastColumn()
```

em vez de definir manualmente:

```javascript
getRange("A1:AT5000")
```

Isso permite que o script acompanhe o crescimento da planilha.

---

## Padronizar nomes de parâmetros

Utilizar URLs simples, como:

```text
?aba=base
?aba=publicacao
?aba=contratos
```

Evitar expor diretamente nomes complexos das abas:

```text
?aba=BASE 2024 A 2025
```

---

## Padronizar datas

Preferir:

```text
yyyy-MM-dd
```

Exemplo:

```text
2026-10-22
```

Esse formato reduz problemas de interpretação no Power BI.

---

## Evitar colunas sem nome

Toda coluna utilizada deve possuir um cabeçalho válido.

Exemplo recomendado:

```text
ID
UNIDADE
INSTRUMENTO
DATA_PAGAMENTO
VALOR_REPASSADO
```

Evitar:

```text
Column1
Campo
Valor 1
Sem título
```

---

## Evitar dados sensíveis

Não disponibilizar no endpoint:

- senhas;
- tokens;
- CPF sem necessidade;
- credenciais;
- dados pessoais sensíveis;
- informações restritas.

A publicação como Web App pode tornar os dados acessíveis por meio da URL, dependendo da configuração adotada.

---