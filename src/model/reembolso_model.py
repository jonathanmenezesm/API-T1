from src.model import db # traz a instancia do sqlalchemy
from sqlalchemy.schema import Column, ForeignKey # traz as classes Column e ForeignKey do sqlalchemy
from sqlalchemy import Column, Integer, String, Float, Date, func, DECIMAL # traz as classes Column, Integer, String, Float, Date, func e DECIMAL do sqlalchemy

#para nomear classe, usar PascalCase (primeira letra maiuscula e sem underline)
#criação da classe Reembolso
class Reembolso(db.Model):
    #--------- atributos da tabela -----------
    id = Column(Integer, primary_key=True, autoincrement=True) #chave primaria, não é necessário passar como parâmetro, pois, é autoincrementada pelo banco de dados.
    colaborador = Column(String(100), nullable=False) #colaborador
    empresa = Column(String(50), nullable=False) #empresa
    num_prestacao = Column(Integer, nullable=False) #numero da prestacao
    descricao = Column(String(255)) #descricao
    data = Column(Date, nullable=False, server_default= func.current_date()) #data
    tipo_reembolso = Column(String(30)) #tipo de reembolso
    centro_custo = Column(String(100)) #centro de custo
    ordem_interna = Column(String(25)) #ordem interna
    divisao = Column(String(25)) #divisao
    pep = Column(String(25)) #pep
    moeda = Column(String(10)) #moeda
    distancia_km = Column(String(255))
    valor_km = Column(DECIMAL(10, 2)) #valor por km
    valor_faturado = Column(DECIMAL(10, 2), nullable=False) #valor faturado
    despesa = Column(DECIMAL(10, 2)) #despesa
    id_colaborador = Column(Integer, ForeignKey(column='colaborador.id'), nullable= False) #chave estrangeira para a tabela colaborador
    status = Column(String(30), nullable=False) #status do reembolso (aprovado, reprovado, pendente)
    #--------- atributos da tabela -----------
    
    #--------- construtor da classe -----------
    def __init__(self, colaborador, empresa, num_prestacao, descricao, data, tipo_reembolso, centro_custo, ordem_interna, divisao, pep, moeda, distancia_km, valor_km, valor_faturado, despesa, id_colaborador, status):
        # self.id = id // o id é gerado automaticamente pelo banco de dados, não sendo necessário passar como parâmetro
        self.colaborador = colaborador
        self.empresa = empresa
        self.num_prestacao = num_prestacao
        self.descricao = descricao
        self.data = data
        self.tipo_reembolso = tipo_reembolso
        self.centro_custo = centro_custo
        self.ordem_interna = ordem_interna
        self.divisao = divisao
        self.pep = pep
        self.moeda = moeda
        self.distancia_km = distancia_km
        self.valor_km = valor_km
        self.valor_faturado = valor_faturado
        self.despesa = despesa
        self.id_colaborador = id_colaborador
        self.status = status
    