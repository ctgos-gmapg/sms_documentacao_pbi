# Qualidade dos dados

## Situação atual

O modelo contém evidência de troubleshooting de tipos (`Erros em Repasses`, `Erros em Repasses (2)` etc.), mas não há uma camada formal de testes de qualidade no artefato analisado.

A recomendação é transformar verificações ad hoc em regras executáveis.

## Testes mínimos

| ID | Regra | Severidade | Motivo |
|---|---|---:|---|
| DQ-001 | `Codigo_OS` não pode ser `0` nem nulo nas quatro fontes | erro | mapping desconhecido não deve ser silencioso |
| DQ-002 | `dim_instituição[Codigo_Os]` deve ser único | erro | requisito do lado dimensão |
| DQ-003 | toda chave institucional dos fatos deve existir em `dim_instituição` | erro | integridade referencial |
| DQ-004 | `Chave_Contrato` não pode ser nula | erro | chave de integração |
| DQ-005 | toda `Chave_Contrato` de fato deve existir em `dim_contrato` | erro | integridade referencial |
| DQ-006 | `Ano_Mes_Ref` / `rfr_id_referencia` devem ser datas válidas | erro | eixo temporal |
| DQ-007 | `Receitas_Painel[ref_mes]` deve estar entre 1 e 12 | erro | evita lógica reparadora |
| DQ-008 | `Despesas_Painel[COD_OS]` deve ser parseável como inteiro | erro | compatibilidade com dimensão |
| DQ-009 | contrato não deve conter `|` | erro | delimitador da chave composta |
| DQ-010 | regra VIVA RIO 015/2023-TC deve ter contagem conhecida/auditável | warning | regra excepcional |

## Testes de reconciliação financeira

Além de schema/integridade, cada refresh deveria registrar pelo menos:

- contagem de linhas por fonte e competência;
- soma de `Repasses[VALOR]` por competência;
- soma do campo de receita efetivamente usado pelo negócio;
- soma de `Despesas_Painel[Valor_Pago]` por competência;
- soma de `Piso_Enfermagem[pe_complemento_mensal]` por competência;
- variação percentual contra a carga anterior.

Thresholds de anomalia precisam ser definidos pelo domínio. O repositório não possui evidência suficiente para inventar limites.

## Fail fast

Mappings desconhecidos não devem resultar em `Codigo_OS = 0`. O comportamento recomendado é:

1. preservar o valor bruto;
2. tentar resolver via dimensão de referência;
3. classificar os não resolvidos como rejeitados/quarentena;
4. falhar a validação ou emitir alerta explícito.
