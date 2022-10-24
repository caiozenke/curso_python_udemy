"""
Private , Public , Protected

Public -Atributo acessivel
_ Protected - Atributo fica oculto , porém acessivel fora da classe
__ Private - Atributo inacessivel , cria outro atributo com mesmo nome caso seja passado fora da classe

"""

class BaseDeDados:
    def __init__(self):
        self.__dados={}

    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id :nome.lower()}
        else:
            self.__dados['clientes'].update({id:nome.lower()})
    

    def apagar_cliente(self, id):
        if id in self.__dados['clientes']:
            del self.__dados['clientes'][id]
        else:
            print(f'não existe nenhum cliente com id:{id}')


    def listar_clientes(self):
        print('Lista de Clientes:' )
        for id,nm in self.__dados['clientes'].items():
            
            print(f'\t{id} : {nm}')

db = BaseDeDados()

db.inserir_cliente(3,'Caio')
db.inserir_cliente(1,'zenke')
db.inserir_cliente(2,'Luan')
db.apagar_cliente(3)
db.__dados= 'aaaaaaaaaaaa' #cria um setter nao prejudicando os atributos originais 
db.listar_clientes()