import re
from utils.storage import salvar_usuarios

# Lista de palavras comuns que devem ser evitadas
dicionario = ["password", "123456", "admin", "user", "qwerty"]

# Função para verificar a senha
def verificar_requisitos_senha(usuario, senha):
    requisitos = {}

    # Regra 1: Verificar o tamanho mínimo
    requisitos['Pelo menos 8 caracteres'] = len(senha) >= 8
    
    # Regra 2: Verificar a presença de letras maiúsculas
    requisitos['Pelo menos uma letra maiúscula'] = bool(re.search(r'[A-Z]', senha))
    
    # Regra 3: Verificar a presença de letras minúsculas
    requisitos['Pelo menos uma letra minúscula'] = bool(re.search(r'[a-z]', senha))
    
    # Regra 4: Verificar a presença de números
    requisitos['Pelo menos um número'] = bool(re.search(r'[0-9]', senha))
    
    # Regra 5: Verificar a presença de símbolos
    requisitos['Pelo menos um símbolo'] = bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', senha))
    
    # Regra 6: Verificar se a senha contém o nome do usuário (case-insensitive)
    if usuario:
        usuario_lower = usuario.lower()
        senha_lower = senha.lower()
        requisitos['Não conter o nome do usuário'] = usuario_lower not in senha_lower
    else:
        requisitos['Não conter o nome do usuário'] = False  # Impede que passe se o usuário estiver vazio
    
    # Regra 7: Verificar se a senha contém palavras do dicionario
    requisitos['Não conter palavras comuns'] = not any(word in senha.lower() for word in dicionario)
    
    return requisitos

def verificar_usuario(usuario):
    if not usuario:  # Verifica se o usuário está vazio ou é None
        return "Usuário não fornecido ou inválido."
    return None

# Função para realizar o login
def login(usuario, senha, usuarios):
    if usuario in usuarios and usuarios[usuario] == senha:
        return "Login realizado com sucesso!"
    else:
        return "Login falhou. Usuário ou senha incorretos."

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuario, senha, usuarios):
    mensagem_usuario = verificar_usuario(usuario)
    if mensagem_usuario:
        return mensagem_usuario  # Retorna imediatamente se o usuário for inválido
    
    if usuario in usuarios:
        return "Usuário já existe."
    else:
        requisitos = verificar_requisitos_senha(usuario, senha)
        
        if all(requisitos.values()):
            usuarios[usuario] = senha
            salvar_usuarios(usuarios)
            return "Usuário cadastrado com sucesso!"
        else:
            mensagem = "Senha inválida. Requisitos não atendidos:"
            for requisito, atendido in requisitos.items():
                if not atendido:
                    mensagem += f"\n- {requisito}"
            return mensagem
