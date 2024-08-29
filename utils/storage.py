import json

# Caminho do arquivo onde os dados serão armazenados
ARQUIVO_USUARIOS = "usuarios.json"

# Função para carregar os usuários do arquivo JSON
def carregar_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar os usuários no arquivo JSON
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f)