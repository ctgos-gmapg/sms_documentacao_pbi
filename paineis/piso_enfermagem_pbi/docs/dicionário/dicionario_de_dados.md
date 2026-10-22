# Dicionário de dados

Catálogo técnico e funcional do modelo semântico. Cada coluna aparece em uma linha com seu tipo e sua descrição. A origem é informada uma vez por tabela.

## `Repasses`

**Origem:** Google Sheets publicado como CSV, processado por `Web.Contents` e `Csv.Document`.

| Coluna | Tipo | Descrição |
|---|---|---|
| `UG` | `int64` | Código da unidade gestora responsável pelo repasse. |
| `UNIDADE` | `string` | Nome ou identificação da unidade administrativa. |
| `FAVORECIDO` | `string` | Pessoa ou organização favorecida pelo repasse. |
| `INSTRUMENTO` | `string` | Instrumento administrativo que fundamenta o repasse. |
| `SUBSECRETARIA` | `string` | Subsecretaria responsável pelo registro. |
| `PROCESSO SEI` | `string` | Identificador do processo no SEI. |
| `EXERCÍCIO` | `int64` | Ano fiscal do registro. |
| `TERMO ADITIVO` | `string` | Identificação do termo aditivo associado. |
| `NATUREZA DE DESPESA` | `string` | Classificação orçamentária da despesa. |
| `DOCUMENTO DE REPASSE` | `string` | Identificação do documento de repasse. |
| `DOC.SEI DOCUMENTO REPASSE` | `int64` | Número do documento SEI do repasse. |
| `DOC.SEI RESPONSÁVEL ASSINATURA ELD` | `int64` | Número do documento SEI relacionado ao responsável pela assinatura. |
| `EMPENHO` | `string` | Número ou identificação do empenho. |
| `FONTE` | `int64` | Código da fonte de recursos. |
| `COMPETÊNCIA` | `string` | Período de competência informado na origem. |
| `VALOR` | `double` | Valor financeiro do repasse. |
| `Nº NL` | `string` | Número da nota de liquidação. |
| `EMISSOR DA NL` | `string` | Emissor da nota de liquidação. |
| `Nº NL ANULADA` | `string` | Número da nota de liquidação anulada, quando houver. |
| `STATUS` | `string` | Situação atual do registro. |
| `Nº DA PD` | `string` | Número da programação de desembolso. |
| `DATA DA PD` | `string` | Data da programação de desembolso conforme recebida da fonte. |
| `EMISSOR DA PD` | `string` | Emissor da programação de desembolso. |
| `Nº PD ANULADA` | `string` | Número da programação de desembolso anulada, quando houver. |
| `GD` | `string` | Identificador ou classificação GD da origem. |
| `BLOQUEIO` | `string` | Indicador ou motivo de bloqueio do registro. |
| `DATA DE PAGAMENTO` | `dateTime` | Data efetiva do pagamento. |
| `DATA DEVOLUÇÃO PROCESSO SUBSECRETARIA` | `dateTime` | Data de devolução do processo à subsecretaria. |
| `QUANTIDADE DE FRAGILIDADE` | `int64` | Quantidade de ocorrências de fragilidade registrada. |
| `OBSERVAÇÃO` | `string` | Observações livres sobre o repasse. |
| `Codigo_OS` | `int64` | Código numérico padronizado da organização social, calculado por regra DAX. |
| `ID` | `string` | Identificador composto do registro, formado pela concatenação de campos de negócio. |
| `Ano_Mes_Ref` | `dateTime` | Primeiro dia do mês de referência usado no calendário. |
| `Chave_Contrato` | `string` | Chave composta usada para relacionar organização social e contrato. |

## `Receitas_Painel`

**Origem:** arquivo Excel local `receitas_painel.xlsx`, aba `Sheet1`.

| Coluna | Tipo | Descrição |
|---|---|---|
| `id_receita_dados` | `int64` | Identificador do registro de dados de receita. |
| `cod_unidade` | `int64` | Código da unidade associada à receita. |
| `id_contrato` | `int64` | Identificador do contrato. |
| `ref_mes` | `string` | Mês de referência da receita, normalizado no Power Query. |
| `ref_ano` | `int64` | Ano de referência da receita. |
| `id_receita_item` | `int64` | Identificador do item de receita. |
| `flg_ativo` | `string` | Indicador de registro ativo. |
| `valor` | `int64` | Valor principal registrado para a receita. |
| `id_conta_bancaria` | `int64` | Identificador da conta bancária. |
| `id_termo_aditivo` | `int64` | Identificador do termo aditivo. |
| `descricaoUnidade` | `string` | Descrição da unidade. |
| `numeroContrato` | `string` | Número do contrato. |
| `descricaoReceitaItem` | `string` | Descrição do item de receita. |
| `descricaoBanco` | `string` | Nome ou descrição do banco. |
| `descricaoAgencia` | `string` | Descrição da agência bancária. |
| `descricaoContaCorrente` | `string` | Descrição da conta corrente. |
| `budgetMngtFixedValue` | `double` | Valor fixo de gestão orçamentária. |
| `budgetMngtVariable1Value` | `double` | Primeiro componente variável de gestão orçamentária. |
| `budgetAddCustTAValue` | `double` | Valor adicional de custeio do termo aditivo. |
| `budgetAddInvesTAValue` | `double` | Valor adicional de investimento do termo aditivo. |
| `investmentsValue` | `double` | Valor de investimentos. |
| `expensesReverseValue` | `double` | Valor de reversão de despesas. |
| `externalResourcesValue` | `double` | Valor de recursos externos. |
| `loanReverseValue` | `double` | Valor de reversão de empréstimo. |
| `loanAnotherContractValue` | `double` | Valor transferido de outro contrato. |
| `budgetMngtVariable2Value` | `int64` | Segundo componente variável de gestão orçamentária. |
| `budgetMngtVariable3Value` | `int64` | Terceiro componente variável de gestão orçamentária. |
| `transferAccountContractExecValue` | `double` | Valor transferido para execução contratual. |
| `transferResourceAnotherContractValue` | `double` | Recurso transferido de outro contrato. |
| `repaymentIntegrasusValue` | `int64` | Valor de devolução ou ressarcimento Integrasus. |
| `totalValue` | `double` | Valor total calculado ou informado para a receita. |
| `multId` | `string` | Identificador múltiplo da origem. |
| `cod_usuario` | `int64` | Código do usuário responsável pela alteração. |
| `data_alteracao` | `string` | Data da última alteração conforme recebida da origem. |
| `deliveryReport` | `string` | Relatório ou informação de entrega do registro. |
| `ID` | `string` | Identificador composto do registro. |
| `Ano_Mes_Ref` | `dateTime` | Primeiro dia do mês de referência. |
| `Chave_Contrato` | `string` | Chave composta de organização social e contrato. |

## `Despesas_Painel`

**Origem:** arquivo Excel local `despesas_painel.xlsx`, aba `Planilha1`.

| Coluna | Tipo | Descrição |
|---|---|---|
| `Num_Seq` | `int64` | Número sequencial do registro. |
| `Nome_Os` | `string` | Nome da organização social. |
| `Nome_Unidade` | `string` | Nome da unidade. |
| `Num_Contrato` | `string` | Número do contrato. |
| `Ano_Mes_Ref` | `dateTime` | Mês de referência da despesa. |
| `Tipo_Documento` | `string` | Tipo do documento financeiro. |
| `Cnpj` | `string` | CNPJ relacionado ao documento ou favorecido. |
| `Razao` | `string` | Razão social do favorecido. |
| `Cpf` | `string` | CPF relacionado ao documento ou favorecido. |
| `Nome` | `string` | Nome da pessoa ou entidade favorecida. |
| `Serie` | `int64` | Série do documento fiscal ou financeiro. |
| `Descricao` | `string` | Descrição do documento ou lançamento. |
| `Documeto_Existe` | `string` | Indicador de existência do documento. |
| `Data_Emissao` | `dateTime` | Data de emissão do documento. |
| `Data_Vencimento` | `dateTime` | Data de vencimento do documento. |
| `Data_Pagamento` | `dateTime` | Data de pagamento da despesa. |
| `Data_Apuracao` | `dateTime` | Data de apuração da despesa. |
| `Valor_Documento` | `double` | Valor total do documento. |
| `Valor_Pago` | `double` | Valor efetivamente pago. |
| `Despesa` | `string` | Categoria ou descrição da despesa. |
| `Rubrica` | `string` | Rubrica orçamentária. |
| `Pmt_Mes` | `int64` | Parcela ou pagamento acumulado no mês. |
| `Pmt_Total` | `int64` | Total de parcelas ou pagamentos. |
| `Flg_Justificativa` | `string` | Indicador de existência de justificativa. |
| `Conta_Corrente` | `string` | Conta corrente utilizada. |
| `Nome_Agencia` | `string` | Nome ou identificação da agência. |
| `Nome_Banco` | `string` | Nome do banco. |
| `Validado` | `string` | Indicador de validação do registro. |
| `COD_OS` | `string` | Código da organização social na origem. |
| `Column1` | `string` | Coluna auxiliar preservada da planilha de origem. |
| `ID` | `string` | Identificador composto do registro. |
| `Chave_Contrato` | `string` | Chave composta de organização social e contrato. |

## `Piso_Enfermagem`

**Origem:** PostgreSQL `ctgos`, tabela `public.rh_pisoenfermagem`.

| Coluna | Tipo | Descrição |
|---|---|---|
| `pe_cpf` | `string` | CPF do profissional. |
| `pe_nome` | `string` | Nome do profissional. |
| `pe_cnes` | `int64` | Código CNES da unidade ou estabelecimento. |
| `pe_cbo` | `int64` | Código Brasileiro de Ocupações. |
| `pe_jornada_semanal` | `int64` | Carga horária semanal. |
| `pe_salario_base` | `double` | Salário base do profissional. |
| `pe_remuneracao_mensal` | `double` | Remuneração mensal. |
| `pe_insalubridade` | `double` | Valor do adicional de insalubridade. |
| `pe_adicional_noturno` | `double` | Valor do adicional noturno. |
| `pe_encargo_patronal` | `double` | Encargo patronal. |
| `pe_encargo_trabalhista` | `double` | Encargo trabalhista. |
| `pe_vantagem_fixa` | `double` | Valor de vantagens fixas. |
| `pe_vantagem_variavel` | `double` | Valor de vantagens variáveis. |
| `pe_complemento_mensal` | `double` | Complemento mensal. |
| `pe_contrato` | `string` | Número ou identificação do contrato. |
| `pe_organizacao_social` | `string` | Organização social responsável. |
| `pe_uo` | `int64` | Código da unidade orçamentária. |
| `pe_pt` | `string` | Programa de trabalho ou classificação PT. |
| `pe_subsecretaria` | `string` | Subsecretaria responsável. |
| `pe_unidade_saude` | `string` | Unidade de saúde vinculada. |
| `rfr_id_referencia` | `dateTime` | Data de referência da remuneração. |
| `Codigo_OS` | `int64` | Código numérico padronizado da organização social. |
| `ID` | `string` | Identificador composto do registro. |
| `Chave_Contrato` | `string` | Chave composta de organização social e contrato. |

## Dimensões

### `dim_contrato`

Dimensão de contratos usada para relacionar as tabelas transacionais.

| Coluna | Tipo | Descrição |
|---|---|---|
| `Chave_Contrato` | `string` | Chave única da combinação entre organização social e contrato. |
| `Codigo_Os` | `int64` | Código numérico da organização social do contrato. |
| `Instrumento` | `string` | Instrumento associado ao contrato. |
| `Nome_Os` | `string` | Nome da organização social. |

### `dim_instituição`

Dimensão de organizações sociais. Derivada a partir de `Repasses`.

| Coluna | Tipo | Descrição |
|---|---|---|
| `Nome_Os` | `string` | Nome da organização social. |
| `Codigo_Os` | `int64` | Código numérico da organização social. |

### `dim_data`

Calendário oficial usado nos relacionamentos de data do modelo.

| Coluna | Tipo | Descrição |
|---|---|---|
| `Data` | `dateTime` | Data do calendário oficial. |
| `Ano` | `int64` | Ano da data. |
| `Mes_Numero` | `int64` | Número do mês. |
| `Mes_Nome` | `string` | Nome do mês. |
| `Ano_Mes` | `string` | Rótulo de ano e mês para análise. |

## Tabela auxiliar

### `Medida`

Tabela técnica criada no Power BI para apoio ao modelo.

| Coluna | Tipo | Descrição |
|---|---|---|
| `Coluna 1` | `null` | Coluna auxiliar aguardando desenvolvimento de medida. |

## Observações

- Os nomes das colunas foram preservados exatamente como aparecem no modelo.
- Os tipos das colunas calculadas foram documentados conforme o uso observado no modelo; por exemplo, `Codigo_OS` é inteiro e `ID` é texto composto.
- As descrições são funcionais e devem ser revisadas pelo responsável de negócio quando houver definição formal da origem.
