#getter e setter

from calendar import c


class Produto:
    def __init__(self,nome, preco):
        self.preco = preco
        self.nome = nome
        
    def desconto(self, perc):
        self.preco = self.preco - (self.preco * (perc / 100))
        
        
    #Getter - Pegar
    
    @property
    def nome(self):
        return self._nome
    
    #Setter - Configura
    @nome.setter #configurar oq vai ser alterado
    def nome(self, valor):
        self._nome= valor.title()
       
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$',''))
        
        self._preco = valor

             
            
p1 = Produto('REGATA', 'R$70')
p1.desconto(10)
print(p1.nome, p1.preco)
        
        
#COM CPF PARA FIXAR


class Cliente():
    def __init__(self,cpf):
        self.cpf = cpf
        
    
    #Getter
    
    @property
    def cpf(self):
        return self._cpf
    
    
    #Setter
    @cpf.setter
    
    def cpf(self,valor):
        valor = str(valor)
        if len(valor) == 11:
            valor = f'{valor[:3]}.{valor[3:6]}.{valor[6:9]}-{valor[9:11]}'
        
        self._cpf= valor
 
from random import randint

v  = randint(10000000000,99999999999)
c1 = Cliente(v)
print(c1.cpf)