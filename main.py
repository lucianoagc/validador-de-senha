import streamlit as st
from utils.auth import login,cadastrar_usuario
from utils.storage import carregar_usuarios

# Carregar usuários do arquivo
usuarios = carregar_usuarios()

# Interface do Streamlit
st.title("Sistema de Login")

opcao = st.selectbox("Selecione a opção", ["Login", "Cadastrar"])

usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if opcao == "Login":
    if st.button("Login"):
        mensagem = login(usuario, senha, usuarios)
        st.write(mensagem)

elif opcao == "Cadastrar":
    if st.button("Cadastrar"):
        mensagem = cadastrar_usuario(usuario, senha, usuarios)
        st.write(mensagem)
