from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import db
# import traceback

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')

# Rota para criar um novo reembolso
@bp_reembolso.route('/refunds/new', methods=['POST', 'OPTIONS'])
def cadastrar_reembolsos():
    # print(f"Método recebido: {request.method}")  # Log do método HTTP recebido

    if request.method == 'OPTIONS':
        # Responde ao preflight
        return jsonify({'message': 'Preflight OK'}), 200

    if request.method == 'POST':
        dados_requisicao = request.get_json()
        # print(f"Dados recebidos: {dados_requisicao}")  # Log dos dados recebidos

        if not isinstance(dados_requisicao, list):
            return jsonify({'erro': 'Os dados enviados devem ser uma lista de reembolsos.'}), 400

        try:
            reembolsos = []
            for dados in dados_requisicao:
                novo_reembolso = Reembolso(
                    colaborador=dados['colaborador'],
                    empresa=dados['empresa'],
                    num_prestacao=dados['prestacaoContas'],
                    descricao=dados['descricaoMotivo'],
                    data=dados['data'],
                    tipo_reembolso=dados['tipoDespesa'],
                    centro_custo=dados['centroCusto'],
                    ordem_interna=dados.get('ordemInterna', ''),
                    divisao=dados.get('divisao', ''),
                    pep=dados.get('pep', ''),
                    moeda=dados['moeda'],
                    distancia_km=dados['distancia'],
                    valor_km=dados['valorKm'],
                    valor_faturado=dados['valorFaturado'],
                    despesa=dados['despesa'],
                    id_colaborador=1, # ID do colaborador fixo para teste, deve ser alterado para pegar o ID do colaborador logado (estudar JWT)
                    status="Pendente"
                )
                reembolsos.append(novo_reembolso)

            db.session.add_all(reembolsos)
            db.session.commit()

            return jsonify({'mensagem': 'Reembolsos cadastrados com sucesso!'}), 201

        except Exception as e:
            # traceback.print_exc()  # Exibe o traceback completo no terminal
            return jsonify({'erro': f'Ocorreu um erro ao cadastrar os reembolsos: {str(e)}'}), 500
        
# Rota para buscar reembolsos pelo número da prestação de contas
@bp_reembolso.route('/refunds/<int:num_prestacao>', methods=['GET'])
def buscar_reembolsos_por_prestacao(num_prestacao):
    try:
        reembolsos = Reembolso.query.filter_by(num_prestacao=num_prestacao).all()

        if not reembolsos:
            return jsonify({'mensagem': f'Nenhum reembolso encontrado com Nº Prest. Contas {num_prestacao}'}), 404

        resultado = []
        for r in reembolsos:
            resultado.append({
                'id': r.id,
                'colaborador': r.colaborador,
                'empresa': r.empresa,
                'num_prestacao': r.num_prestacao,
                'descricao': r.descricao,
                'data': r.data.strftime('%Y-%m-%d'),
                'tipo_reembolso': r.tipo_reembolso,
                'centro_custo': r.centro_custo,
                'ordem_interna': r.ordem_interna,
                'divisao': r.divisao,
                'pep': r.pep,
                'moeda': r.moeda,
                'distancia_km': r.distancia_km,
                'valor_km': float(r.valor_km or 0),
                'valor_faturado': float(r.valor_faturado or 0),
                'despesa': float(r.despesa or 0),
                'status': r.status
            })

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro ao buscar os reembolsos: {str(e)}'}), 500
