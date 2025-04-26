importpytest
from src.model.colaborador_model import Colaborador
import time

# ------------- configurações -------------
@pytest.fixture
def app():
    app = create_app()
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()

#------------------------------------------


def test_pegar_todos_colaboradores(client):
    responsta = client.get('/colaboradores')
    assert resposta.status_code == 200
    # assert b'Colaboradores' in response.data


def test_desempenho_requisicao_get(client):
    comeco = time.time()  # Inicia o cronômetro
    # Faz 100 requisições para o endpoint /colaboradores
    
    for _ in range(100):
        resposta = client.get('/colaboradores')
    
    resposta = client.get('/colaboradores')
    fim = time.time() - comeco # Para o cronômetro 
       
    assert fim < 1.0  # Verifica se a requisição levou menos de 1 segundo