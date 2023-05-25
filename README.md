## Como iniciar

Para ligar o projeto, você precisa seguir os seguintes passos:

- Instale o Python 3.9 ou superior na sua máquina. Você pode baixar o Python do site oficial: https://www.python.org/downloads/
- Instale o MongoDB 5.0.4 ou superior na sua máquina ou em um servidor remoto. Você pode baixar o MongoDB do site oficial: https://www.mongodb.com/try/download/community
- Clone este repositório usando o comando: `git clone https://github.com/zLucfx/login-flask.git`
- Edite o arquivo `app.py` e altere os valores das variáveis `SECRET_KEY` e `MONGO_URI` para os valores desejados. A `SECRET_KEY` é usada para proteger os dados da sessão dos usuários e deve ser um valor aleatório e secreto. A `MONGO_URI` é a URI de conexão com o MongoDB e deve conter as informações do host, da porta, do usuário, da senha e do banco de dados do MongoDB. Por exemplo: `mongodb://localhost:27017/login`
- Execute o comando: `python run.py`
- Acesse o site pelo endereço `http://localhost:5000`
