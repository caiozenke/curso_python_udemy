from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))#Instancia da classe
    
    
    def __init__(self,nome ,idade) -> None:
        self.nome = nome 
        self.idade = idade
        
        
    #metodo de classes = CLS     
    @classmethod
                    #cls no lugar do self, e os args
    def criar_nascimento(cls,nome, ano_nascimento):
            idade = cls.ano_atual - ano_nascimento
            return cls(nome, idade) #retorna o nome e iade com base do ano passado
 
            
p1 = Pessoa.criar_nascimento('caio', 2005)
print(p1.nome , p1.idade)
