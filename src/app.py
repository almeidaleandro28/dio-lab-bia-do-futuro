import pandas as pd
import streamlit as st
import ollama

# # datas
# inventario = pd.read_csv('./data/Inventario.csv')
# produtos = pd.read_csv('./data/Productos.csv')
# lojas = pd.read_csv('./data/Tiendas.csv')
# vendas = pd.read_csv('./data/Ventas.csv')

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Junior - Controlador de Inventário", page_icon="📦")

# --- CARREGAMENTO DE DADOS (Base de Conhecimento) ---
@st.cache_data
def load_data():
    try:
        inventario = pd.read_csv('./data/Inventario.csv')
        produtos = pd.read_csv('./data/Productos.csv')
        lojas = pd.read_csv('./data/Tiendas.csv')
        vendas = pd.read_csv('./data/Vientas.csv')
        return inventario, produtos, lojas, vendas
    except FileNotFoundError:
        st.error("Erro: Arquivos CSV não encontrados na pasta /data.")
        return None, None, None, None

df_inv, df_prod, df_lojas, df_vendas = load_data()

# --- CONSTRUÇÃO DO CONTEXTO PARA O LLM ---
def build_context():
    contexto = f"""
    DADOS DO INVENTARIO:
    {df_inv.to_string(index=False)}
    
    DADOS DOS PRODUTOS:
    {df_prod.to_string(index=False)}
    
    DADOS DAS LOJAS:
    {df_lojas.to_string(index=False)}
    
    DADOS DAS VENDAS:
    {df_vendas.to_string(index=False)}
    
    REGRAS DE NEGÓCIO:
    - Margem: Preço - Custo.
    - Estoque Crítico: Abaixo de 20 unidades.
    - Estoque Saudável: Acima de 100 unidades.
    """
    return contexto

# --- INTERFACE ---
st.title("📦 Junior - Controlador de Inventário")
st.markdown("---")

# Inicializar histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Usuário
if prompt := st.chat_input("Pergunte sobre o estoque ou vendas..."):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparar o System Prompt baseado no seu documento 03-prompts.md
    system_prompt = f"""
    Você é o Junior, um Controlador de Inventário Inteligente.
    Seu objetivo é ajudar a entender o controle de inventário de forma educativa e direta.
    
    PERSONA:
    - Educativo, paciente e direto.
    - Tom informal e acessível (como um professor particular).
    - Use os dados fornecidos abaixo para dar exemplos reais.
    
    REGRAS:
    1. Só use os dados fornecidos no contexto.
    2. Se não souber, admita que não tem a informação.
    3. NÃO faça previsões macroeconômicas.
    4. Foque em análise de estoque e rentabilidade.
    
    CONTEXTO ATUAL:
    {build_context()}
    """

    # Chamada ao Ollama
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            response = ollama.chat(
                model='llama3', # Ou o modelo que você tiver baixado (ex: mistral, phi3)
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    *st.session_state.messages
                ],
                stream=True
            )
            
            for chunk in response:
                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Erro ao conectar com Ollama: {e}")