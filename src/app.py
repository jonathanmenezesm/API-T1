# RESPONSÁVEL PELA CRIAÇÃO DA APLICAÇÃO 
# CREATE_APP() => VAI CONFIGURAR A INSTNACIA DO FLASK
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_colaborador)
    
    app.config.from_object(Config) #Traz a configuração do banco de dados para a aplicação
    db.init_app(app) #inicializa o banco de dados com a instância do flask
    
    with app.app_context():
        db.create_all()#cria as tabelas caso nao existam
    
    return app