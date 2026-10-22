# Transformações e regras

Este documento separa transformações de ingestão (Power Query) de regras semânticas (DAX).

## Power Query — Repasses

Pipeline:

1. download de CSV público;
2. promoção de cabeçalhos;
3. cast explícito de 37 colunas;
4. filtro `INSTRUMENTO <> null`;
5. remoção de colunas não usadas no modelo.

Risco principal: schema rígido e dados de data/tipo vindos de fonte colaborativa.

## DAX — Repasses

### Mapping de OS

`FAVORECIDO` é convertido em `Codigo_OS` via cadeia de `IF`. O fallback é `0`.

Esse mapping é dado mestre e deveria existir como tabela de referência, não como lógica de coluna calculada.

### Competência especial

Para:

```text
Codigo_OS = 264
INSTRUMENTO = 015/2023-TC
mês de DATA DE PAGAMENTO = 2023-11
```

`Ano_Mes_Ref` é forçado para `2023-12-01`.

A mesma exceção altera `ID` de `...2023-11` para `...2023-12`.

A duplicação da regra em duas colunas é um risco: uma alteração futura pode ser aplicada em uma e esquecida na outra.

## Power Query — Receitas_Painel

Pipeline:

1. leitura de `Sheet1`;
2. promoção de cabeçalhos;
3. cast de tipos;
4. remoção de `Column1`;
5. filtro `budgetAddCustTAValue <> 0`;
6. conversão de `ref_mes` para texto;
7. padding/correção do mês por múltiplos `ReplaceValue`.

O tratamento de mês deve ser substituído por conversão numérica e formatação determinística. Exemplo conceitual:

```m
Text.PadStart(Text.From(Number.From([ref_mes])), 2, "0")
```

ou, preferencialmente, criar a data diretamente sem depender da representação textual.

## Power Query — Despesas_Painel

Pipeline:

1. leitura de `Planilha1`;
2. promoção de cabeçalhos;
3. cast;
4. remoção de colunas;
5. derivação de `COD_OS` a partir do prefixo de `Nome_Os`.

A extração do código a partir do texto de apresentação é um anti-pattern de integração. O código deveria vir como campo próprio ou ser resolvido por tabela de referência.

## Power Query — Piso_Enfermagem

Pipeline curto:

1. conexão PostgreSQL;
2. seleção de `public.rh_pisoenfermagem`;
3. padronização `VIVA RIO -> VIVARIO`.

Depois do carregamento, DAX volta a mapear o nome para código. Há, portanto, duas etapas de normalização para a mesma entidade.

## Chaves

### `Chave_Contrato`

As quatro tabelas criam uma chave textual no padrão:

```text
Codigo_OS|Contrato
```

A intenção é correta: diferenciar contratos que podem se repetir entre organizações. O problema é o local de implementação e a ausência de validação formal dos componentes.

### `ID`

Existe uma segunda concatenação incluindo competência. Como não há evidência de relacionamento usando `ID`, ela deve ser tratada como chave técnica auxiliar e ter sua finalidade documentada antes de ser usada como identificador único.
