# Validador de Senha

Este é um projeto de estudo focado em Segurança da Informação, que implementa um sistema de criação e validação de senhas para logon. O projeto segue boas práticas de segurança, garantindo que as senhas atendam a requisitos específicos.

## Desenvolvedor:
[Luciano de Castro](https://github.com/lucianoagc)

## Estrutura do Projeto

- `main.py`: Arquivo principal que executa o aplicativo.
- `utils/auth.py`: Módulo responsável pela autenticação e validação das senhas.
- `utils/storage.py`: Módulo que lida com o armazenamento dos dados dos usuários.
- `requirements.txt`: Arquivo que lista as dependências do projeto.
- `.gitignore`: Arquivo de configuração para ignorar arquivos e diretórios no Git.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/validador-de-senha.git
    ```

2. Navegue até o diretório do projeto:

   ```bash
   cd validador-de-senha
   ```

3. Navegue até o diretório do projeto:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

4. Navegue até o diretório do projeto:

   ```bash
    pip install -r requirements.txt
   ```


## Uso

Execute o script principal para iniciar o aplicativo:

```bash
streamlit run main.py
```



O aplicativo irá solicitar a criação de um usuário e senha, garantindo que a senha siga as regras estabelecidas no código.

## Regras de Senha

O validador de senha impõe as seguintes regras para garantir a segurança:

    Mínimo de 8 caracteres.
    Mínimo de uma letra maiúscula.
    Mínimo de uma letra minúscula.
    Mínimo de um número.
    Mínimo de um caractere especial.
    Não conter palavras comuns


## Contribuição

Sinta-se à vontade para contribuir com melhorias e novas funcionalidades para este projeto. Faça um fork do repositório, crie um branch para sua feature e envie um pull request.