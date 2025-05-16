from os import environ #Traz para o arquivo o acesso as variáveis de ambiente.
from dotenv import load_dotenv #Carrega as variáveis de ambiente do arquivo .env

load_dotenv() #Carrega as variáveis de ambiente para este arquivo

class Config():
    # Configuração do banco de dados
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD') #Acessa a variável de ambiente DATABASE_URL (PRODUÇÃO)
    # SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_DEV')
    #Acessa a variável de ambiente DATABASE_URL (DESENVOLVIMENTO)
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Desabilita o rastreamento de modificações do SQLAlchemy para economizar recursos.
