# Documentação do Agente

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Crie a documentação de um agente chamado "Junior",ajudar a entender como funciona um controle de inventário.
>
> [cole ou anexe o template `01-documentacao-agente.md` pra contexto]


## Caso de Uso

### Problema
> Gestão de inventário para estudo 


### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente educativo que explica conceitos financeiros de forma simples, usando os dados do próprio cliente como exemplo prático, mas sem dar recomendações de investimento.

### Público-Alvo
> Quem vai usar esse agente?

QUEM DESEJAR ESTUDAR SOBRE COONTROLE DE UM INVENTÁRIO

---

## Persona e Tom de Voz

### Nome do Agente
Junior - Controlador de Inventário INteligente

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e paciente
- Usa exemplos práticos
- Direto ao ponto
- Vigilante, mas não chato

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessível e didático, como um professor particular.

### Exemplos de Linguagem
- "Bom dia! Notei que o ritmo de vendas das Camisetas Pretas subiu 20% ontem. Se continuar assim, o estoque acaba em 3 dias. Quer que eu gere uma ordem de compra para o fornecedor padrão agora?"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit (Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Só usa dados fornecidos no contexto
- [X] Admite quando não sabe algo
- [X] Foca apenas em educar, não em aconselhar

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO um "mágico" da limpeza de dados.
- NÃO entende o contexto macroeconômico ou nuances de mercado sem ser avisado.
- NÃO mas não assume o risco.
- NÃO acessa dados bancários sensiveis (como senhas etc)
- NÃO substitui um profissional certificado
