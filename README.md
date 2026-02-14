# 🎓 Junior - Controlador de Inventário Inteligente

> Agente de IA Generativa quea ajudar no entendimento de como funcionar um  controle de estoque para loja de pequeno porte.

## 💡 O Que é o Junior?
Junior analisar os arquivo base e mostrar alguns indicadores de como está o estoque quais produtos estão vendendo muito e dá dicas d3e melhoria na gestão do inventário

**O que o Junjior faz:**
- ✅ Retorna algums indicadores
- ✅ Usa dados do inventário da loja para obter resposta
- ✅ Responde dúvidas sobre gestão de inventário
- ✅ Analisa padrões de gestão de almoxerifado para estudo

**O que o Edu NÃO faz:**
- ❌ O agente não pode se conectar a APIs de e-commerce reais, sistemas de pagamento ou bancos de dados externos vivos
- ❌ O agente não pode realizar pedidos de compra reais ou emitir notas fiscais. Ele apenas "sugere" ações em formato de texto para fins acadêmicos.
- ❌ O agente não enviará e-mails ou alertas para fornecedores fictícios.
- ❌ O agente ignorará impostos, taxas de câmbio, inflação ou custos de logística complexos, mantendo o cálculo simples para facilitar o aprendizado.
- ❌ O agente opera apenas com as datas presentes nos arquivos CSV fornecidos
- 

## 🏗️ Arquitetura

```mermaid
flowchart TD
    A[Usuário] --> B[Streamlit]
    B --> C[Ollama - LLM Local]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Resposta Educativa]
```

**Stack:**
- Interface: Streamlit
- LLM: Ollama (modelo local `gpt-oss`)
- Dados: JSON/CSV mockados

## 📁 Estrutura do Projeto

```
├── data/                          # Base de conhecimento
│   ├── perfil_investidor.json     # Perfil do cliente
│   ├── transacoes.csv             # Histórico financeiro
│   ├── historico_atendimento.csv  # Interações anteriores
│   └── produtos_financeiros.json  # Produtos para ensino
│
├── docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md  # Caso de uso e persona
│   ├── 02-base-conhecimento.md    # Estratégia de dados
│   ├── 03-prompts.md              # System prompt e exemplos
│   ├── 04-metricas.md             # Avaliação de qualidade
│   └── 05-pitch.md                # Apresentação do projeto
│
└── src/
    └── app.py                     # Aplicação Streamlit
```

## 🚀 Como Executar

### 1. Instalar Ollama

```bash
# Baixar em: ollama.com
ollama pull gpt-oss
ollama serve
```

### 2. Instalar Dependências

```bash
pip install streamlit pandas requests
```

### 3. Rodar o Edu

```bash
streamlit run src/app.py
```

## 🎯 Exemplo de Uso

**Pergunta:** "O que é CDI?"  
**Edu:** "CDI é uma taxa de referência usada pelos bancos. Quando um investimento rende '100% do CDI', significa que ele acompanha essa taxa. Hoje o CDI está próximo da Selic. Quer que eu explique a diferença entre os dois?"

**Pergunta:** "Onde estou gastando mais?"  
**Edu:** "Olhando suas transações de outubro, sua maior despesa é moradia (R$ 1.380), seguida de alimentação (R$ 570). Juntas, representam quase 80% dos seus gastos. Isso é bem comum! Quer que eu explique algumas estratégias de organização?"

## 📊 Métricas de Avaliação

| Métrica | Objetivo |
|---------|----------|
| **Assertividade** | O agente responde o que foi perguntado? |
| **Segurança** | Evita inventar informações (anti-alucinação)? |
| **Coerência** | A resposta é adequada ao perfil do cliente? |

## 🎬 Diferenciais

- **Personalização:** Usa os dados do próprio cliente nos exemplos
- **100% Local:** Roda com Ollama, sem enviar dados para APIs externas
- **Educativo:** Foco em ensinar, não em vender produtos
- **Seguro:** Estratégias de anti-alucinação documentadas

## 📝 Documentação Completa

Toda a documentação técnica, estratégias de prompt e casos de teste estão disponíveis na pasta [`docs/`](./docs/).
