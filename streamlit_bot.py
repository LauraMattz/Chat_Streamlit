import streamlit as st
import pandas as pd
import spacy
import streamlit_analytics
import mixpanel

mp = mixpanel.Mixpanel(token='34c02c8da1ba2e6c9fbf94ea1ba80dbb')


nlp = spacy.load('pt_core_news_sm')

# Definir estilo da página
st.set_page_config(page_title="Chatbot", page_icon=":robot_face:")

# Definir título e subtítulo da página
st.title("Chatbot da Laura 🤖")
st.markdown("<h3 style='text-align: center; color: #F63366'>Sou um chatbot e estou aqui para responder suas perguntas! 😄</h3>", unsafe_allow_html=True)


def adicionar_pergunta_resposta(pergunta, resposta):
    global df
    nova_linha = pd.DataFrame({'Pergunta': [pergunta], 'Resposta': [resposta]})
    df = pd.concat([df, nova_linha], ignore_index=True)
    
# Exemplo de perguntas e respostas
exemplos = [
    {'Pergunta': 'Qual é o seu nome?', 'Resposta': 'Meu nome é Chatbot.'},
    {'Pergunta': 'Qual é a sua função?', 'Resposta': 'Minha função é ajudá-lo a responder suas perguntas.'},
    {'Pergunta': 'Qual é o seu objetivo?', 'Resposta': 'Meu objetivo é facilitar sua vida respondendo suas dúvidas.'},
    {'Pergunta': 'O que você sabe fazer?', 'Resposta': 'Eu sou capaz de responder perguntas e fornecer informações.'},
    {'Pergunta': 'Como posso te ajudar?', 'Resposta': 'Você pode me fazer perguntas ou solicitar informações.'},
    {'Pergunta': 'Qual é o seu propósito?', 'Resposta': 'Meu propósito é tornar a comunicação mais fácil e rápida.'},
    {'Pergunta': 'O que é inteligência artificial?', 'Resposta': 'Inteligência artificial é uma área da ciência da computação que busca criar máquinas e sistemas capazes de aprender e tomar decisões.'},
]

# Exibir pergunta selecionada
pergunta_selecionada = st.selectbox("Escolha uma pergunta:", [exemplo['Pergunta'] for exemplo in exemplos])

# Exibir lista de perguntas
df = pd.DataFrame(columns=['Pergunta', 'Resposta'])
for exemplo in exemplos:
    adicionar_pergunta_resposta(exemplo['Pergunta'], exemplo['Resposta'])

# Buscar a resposta no DataFrame
if pergunta_selecionada:
    resposta = df[df['Pergunta'] == pergunta_selecionada]['Resposta'].iloc[0]
else:
    resposta = ""
    
# Registrar evento no Mixpanel
mp.track('Pergunta selecionada', {'pergunta': pergunta_selecionada})

# Exibir resposta
if resposta:
    st.markdown("<div style='background-color: #F63366; border-radius: 3px; padding: 10px; color: white; text-align: center; margin-top: 20px'>Resposta do Bot ⬇️</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color: #C2F0C2; border-radius: 3px; padding: 10px; color: black; text-align: center; margin-top: 10px; font-size: 16px; text-align: center'>{resposta}</div>", unsafe_allow_html=True)
    st.empty()
