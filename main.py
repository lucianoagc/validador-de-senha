import streamlit as st
from utils.auth import login, cadastrar_usuario, verificar_requisitos_senha
from utils.storage import carregar_usuarios

def exibir_requisitos_senha(usuario, senha):
    requisitos = verificar_requisitos_senha(usuario, senha)
    
    st.subheader("Requisitos da Senha:")
    for requisito, atendido in requisitos.items():
        if requisito == "Não conter o nome do usuário" and not usuario:
            continue  # Não exibe este requisito se o usuário não foi fornecido
        if atendido:
            st.markdown(f"✅ **{requisito}**")
        else:
            st.markdown(f"❌ **{requisito}**")


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
    exibir_requisitos_senha(usuario, senha)
    if st.button("Cadastrar"):
        mensagem = cadastrar_usuario(usuario, senha, usuarios)
        st.write(mensagem)