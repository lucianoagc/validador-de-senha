import re
from utils.storage import salvar_usuarios

# Dicionário de palavras comuns que devem ser evitadas
dicionario = ["password", "123456", "admin", "user", "qwerty"]

# Função para verificar a senha
def verificar_senha(usuario, senha):
    # Regra 1: Verificar o tamanho mínimo
    if len(senha) < 6:
        return "Senha deve ter pelo menos 6 caracteres."
    
    # Regra 2: Verificar a presença de letras maiúsculas, minúsculas, números e símbolos
    if not re.search(r'[A-Z]', senha):
        return "Senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r'[a-z]', senha):
        return "Senha deve conter pelo menos uma letra minúscula."
    if not re.search(r'[0-9]', senha):
        return "Senha deve conter pelo menos um número."
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', senha):
        return "Senha deve conter pelo menos um símbolo."
    
    # Regra 3: Verificar se a senha contém o nome do usuário
    if usuario.lower() in senha.lower():
        return "Senha não deve conter o nome de usuário."
    
    # Regra 4: Verificar se a senha contém palavras do dicionário
    if any(word in senha.lower() for word in dicionario):
        return "Senha não deve conter palavras comuns."
    
    return None

# Função para realizar o login
def login(usuario, senha, usuarios):
    if usuario in usuarios and usuarios[usuario] == senha:
        return "Login realizado com sucesso!"
    else:
        return "Login falhou. Usuário ou senha incorretos."

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuario, senha, usuarios):
    if usuario in usuarios:
        return "Usuário já existe."
    else:
        mensagem = verificar_senha(usuario, senha)
        if mensagem is None:
            usuarios[usuario] = senha
            salvar_usuarios(usuarios)
            return "Usuário cadastrado com sucesso!"
        else:
            return f"Senha inválida: {mensagem}"