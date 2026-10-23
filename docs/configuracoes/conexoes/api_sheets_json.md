# Criando uma API JSON com Google Apps Script

Este documento apresenta, em alto nível, uma abordagem para disponibilizar dados do Google Sheets em formato JSON utilizando Google Apps Script.

A solução pode ser utilizada por aplicações e ferramentas analíticas, como o Power BI.

!!! info "Escopo"
    Esta documentação apresenta apenas conceitos e padrões gerais. Scripts completos, endpoints reais e configurações específicas do ambiente não são disponibilizados publicamente.

---

## Visão geral

```text
Google Sheets
     ↓
Google Apps Script
     ↓
Web App / Endpoint HTTP
     ↓
JSON
     ↓
Power BI / Aplicação
```

O Apps Script atua como uma camada intermediária entre a planilha e os consumidores dos dados.

---

## Principais responsabilidades

A implementação deve contemplar:

- leitura estruturada da planilha;
- identificação do cabeçalho;
- suporte a diferentes fontes ou abas;
- remoção de registros vazios;
- padronização de tipos e datas;
- geração de resposta JSON;
- tratamento de erros.

---

## Múltiplas fontes

Quando uma mesma planilha possuir diferentes conjuntos de dados, pode ser utilizado um identificador lógico na requisição.

Exemplo conceitual:

```text
?aba=base
?aba=referencia
```

O mapeamento entre o identificador e a estrutura física da planilha deve permanecer na implementação.

---

## Consumo no Power BI

O fluxo de consumo pode ser representado como:

```text
Endpoint
   ↓
JSON
   ↓
Power Query
   ↓
Transformações
   ↓
Modelo semântico
```

Recomenda-se realizar tipagem explícita, tratamento de erros e validação da estrutura retornada.

---

## Boas práticas

- utilizar nomes de campos consistentes;
- evitar intervalos fixos;
- padronizar datas;
- validar alterações estruturais na planilha;
- manter configuração separada da lógica principal;
- não expor detalhes desnecessários da infraestrutura.

!!! warning "Segurança"
    Não publique credenciais, tokens, endpoints internos, dados restritos ou informações sensíveis.

---

## Resultado esperado

O objetivo é disponibilizar uma camada estruturada de integração entre uma planilha e seus consumidores, preservando a separação entre documentação pública e detalhes internos de implementação.