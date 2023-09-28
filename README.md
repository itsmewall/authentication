# User Authentication App

Este é um aplicativo de registro e login de usuários construído com o Django. Ele permite que os usuários se registrem, façam login e gerenciem seus perfis.

## Pré-requisitos

Antes de iniciar, certifique-se de que você tenha o seguinte instalado:

- Python 3.x
- pip

## Instalação

1. Clone este repositório:

        git clone https://github.com/seu-usuario/user-authentication-app.git

2. avegue até o diretório do projeto:

            cd user-authentication-app

3. Crie um ambiente virtual (opcional, mas recomendado):

            python -m venv venv

#### Ative o ambiente virtual (Linux/macOS):

            source venv/bin/activate

#### Ative o ambiente virtual (Windows):

            venv\Scripts\activate

4. Instale as dependências do projeto:

            pip install -r requirements.txt

5. Uso
Inicie o servidor de desenvolvimento:

            python manage.py runserver

5. Abra um navegador da web e acesse http://localhost:8000/ para fazer login ou http://localhost:8000/register para se registrar.

6. Após fazer login, você será redirecionado para o perfil do usuário em http://localhost:8000/profile, onde poderá visualizar e editar suas informações de perfil.

## Contribuição
Se deseja contribuir com este projeto, siga estas etapas:

- Faça um Fork do projeto.
- Crie sua Branch de recurso (git checkout -b feature/RecursoIncrivel).
- Faça commit de suas alterações (git commit -m 'Adicione um Recurso Incrível').
- Faça push para a Branch (git push origin feature/RecursoIncrivel).
- Abra uma solicitação de pull.