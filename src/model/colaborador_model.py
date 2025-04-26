from src.model import db #traz a instnacia do sqlalquemy para o arquivo
from sqlalchemy import Column #traz os recursos que transforma atributos em colunas
from sqlalchemy.types import String, DECIMAL, Integer #importa o tipo de dado para as colunas

class Colaborador (db.Model): #db.Model -> mapear e criar a tabela
  #------------------------ ATRIBUTOS ------------------------  
    id = Column(Integer, primary_key=True, autoincrement=True) #Cria a coluna id como chave primária e autoincrementável
    
    nome = Column(String(255)) #Cria a coluna nome como string de 255 caracteres
    email = Column(String(150)) #Cria a coluna email como string de 255 caracteres
    senha = Column(String(50)) #Cria a coluna senha como string de 255 caracteres
    cargo = Column(String(50)) #Cria a coluna cargo como string de 255 caracteres
    salario = Column(DECIMAL) #Cria a coluna salario como decimal 
    
    #----------------------------------------------------------
    
    #------------------------ CONSTRUTOR ----------------------
    
    #método dunder init é um método construtor
    def _init__ (self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
    #----------------------------------------------------------
    
    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha
        }
    #Método to_dict() converte os dados do colaborador em um dicionário
      