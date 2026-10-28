# 🔍 Power Query: Inserção de Data de Atualização

Este documento explica passo a passo o código M utilizado no Power Query do Power BI para:

- Conectar-se a um banco PostgreSQL via ODBC;
- Navegar até um `schema` e uma `view` específicos;
- Transformar tipos de colunas;
- Adicionar uma **coluna com a data/hora do último refresh do Power BI** (`DateTime.LocalNow()`).

---

## 🧠 Objetivo do Código

Permitir que os dados carregados a partir do PostgreSQL tragam consigo a informação de **quando foram atualizados no Power BI**, facilitando:

- Auditoria de dashboards;
- Exibição em visuais como "Dados atualizados em...";
- Garantia de que os dados estão atualizados sem depender do agendamento externo.

Para adicionar a **data/hora da última atualização do Power BI** à sua **consulta existente no Power Query**, você não deve alterar essa consulta principal diretamente. Em vez disso, você deve **criar uma nova consulta separada** chamada, por exemplo, `Atualizacao`, que captura a data/hora atual no momento do **refresh**.


---

### ✅ ETAPA 1 – Crie a Tabela de Atualização

No Power BI:

- **1.** Vá em **Transformar Dados** (abre o Power Query).
- **2.** Clique em **"Nova Fonte" > "Consulta em branco"**.
- **3.** Vá em **"Exibir Editor Avançado"**.
- **4.** Substitua o conteúdo por:

```m
let
    Fonte = #table(
        {"DataAtualizacao"},
        {{ DateTimeZone.RemoveZone(DateTimeZone.UtcNow() - #duration(0,3,0,0)) }}
    )
in
    Fonte
```

- **5.** Clique em "Fechar e Aplicar".
- **6.** Renomeie a tabela como `Atualizacao`.

---

### ✅ ETAPA 2 – Criar a medida no DAX

Depois que a tabela `Atualizacao` estiver no seu modelo, crie a medida no Power BI:

```DAX
Data da Última Atualização = 
MAX('Atualizacao'[DataAtualizacao])
```

Se quiser exibir formatada:

```DAX
Data da Última Atualização (Formatada) = 
FORMAT([Data da Última Atualização], "dd/MM/yyyy HH:mm:ss")
```

A principal vantagem de criar uma medida em vez de usar diretamente o valor retornado pelo Power Query é poder controlar de forma consistente o tipo de dados como `Data/Hora`dentro do modelo. Isso garante que o formato seja aplicado corretamente em todos os visuais e cálculos do Power BI, independentemente de como ou onde os dados foram carregados

Use essa medida em um **visual de Cartão (Card)** no seu relatório.

Lembre-se de *ocultar* a medida criada pelo Power Query. 

---
