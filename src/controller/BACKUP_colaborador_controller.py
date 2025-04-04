from flask import Blueprint, request, jsonify
#Flask é um micro framework para criação de aplicações web em python
#blueprint é resposável por criar um grupo de rotas
#request é um recurso do flask que vai facilitar a captura dos dados na requisição
#jsonify é um recurso do flask que vai facilitar a conversão de dicionário para json

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

dados = [
    {'id': 1, 'nome': 'Karynne Moreira', 'cargo': 'Frontend', 'cracha': 1020},
    {'id': 2, 'nome': 'Samuel Silverio', 'cargo': 'Backend', 'cracha': 1070},
    {'id': 3, 'nome': 'Marcos Monte', 'cargo': 'QA', 'cracha': 0000},
    {'id': 4, 'nome': 'Romulo Rosa', 'cargo': 'Devops', 'cracha': 1030},
    {'id': 5, 'nome': 'Jonathan Moura', 'cargo': 'Fullstack', 'cracha': 7070}
    ]


@bp_colaborador.route('/pegar-dados') #/pegar-dados é o endpoint
def pegar_dados(): 
    return dados

@bp_colaborador.route('/cadastrar', methods=['POST'])
def cadastrar_novo_colaborador():
    dados_requisicao = request.get_json() #captura os dados da requisição
    
    novo_colaborador = {
        'id': len(dados) + 1,
        'nome': dados_requisicao['nome'],
        'cracha': dados_requisicao['cracha'],
        'cargo': dados_requisicao['cargo']
    }
    
    dados.append(novo_colaborador) #adiciona o novo colaborador na lista de dados
    
    return jsonify( {'Mensagem:': 'Colaborador cadastrado com sucesso!'} ), 201 

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