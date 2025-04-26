from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db
from src.security.security import hash_senha, checar_senha
#Flask é um micro framework para criação de aplicações web em python
#blueprint é resposável por criar um grupo de rotas
#request é um recurso do flask que vai facilitar a captura dos dados na requisição
#jsonify é um recurso do flask que vai facilitar a conversão de dicionário para json

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

dados = [
    {'id': 1, 'nome': 'Karynne Moreira', 'cargo': 'Frontend', 'cracha': 1020},
    {'id': 2, 'nome': 'Samuel Silverio', 'cargo': 'Backend', 'cracha': 1070},
    {'id': 3, 'nome': 'Marcos Monte', 'cargo': 'QA', 'cracha': 8080},
    {'id': 4, 'nome': 'Romulo Rosa', 'cargo': 'Devops', 'cracha': 1030},
    {'id': 5, 'nome': 'Jonathan Moura', 'cargo': 'Fullstack', 'cracha': 7070}
    ]


@bp_colaborador.route('/pegar-dados') #/pegar-dados é o endpoint
def pegar_dados(): 
    return dados

@bp_colaborador.route('/cadastrar', methods=['POST'])
def cadastrar_novo_colaborador():
    dados_requisicao = request.get_json()  # Captura os dados da requisição
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha=hash_senha(dados_requisicao['senha']),
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )

    #INSERT INTO tb_colaborador (nome, email, senha, cargo, salario) VALUES ('samuel', 'samueltigrao@gmail.com', '1234', 'cliente', '1500)
    db.session.add(novo_colaborador)  # Adiciona o novo colaborador à sessão do banco de dados
    db.session.commit() # Salva as alterações no banco de dados
    return jsonify({'Mensagem:': 'Colaborador cadastrado com sucesso!'}), 201

#Sinaliza que os dados enviados
#endereço/colaborador/atualizar/10030
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_colaborador(id_colaborador):
    
    dados_requisicao = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break
        
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']
            
    return jsonify( {'mensagem': 'Colaborador atualizado com sucesso!'}), 200


@bp_colaborador.route('/login', methods=['POST'])
def login():
    dados_requisicao = request.get_json()
    
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
         
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os dados precisam ser preenchidos!'}), 400
    
    # SELECT * FROM TABELA WHERE email = email
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.email == email)
    ).scalar()  # Retorna a linha de informação ou None(não houve nenhum registro como solicitado)
    
    if not colaborador:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    
    colaborador = colaborador.to_dict()
    #colaborador = colaborador.to_dict() #converte o objeto colaborador em dicionário
    
    if email == colaborador['email'] and checar_senha(senha, colaborador['senha']):
        return jsonify({'mensagem': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'mensagem': 'Credenciais inválidas!'}), 400
    
