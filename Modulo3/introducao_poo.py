from datetime import datetime

class Pessoa:

    #colocamos este atributo aqui pois todos sempre estarão no mesmo ano NUNCA SERÁ DIFERENTE
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

        #init padrao em python 
    def __init__(self, nome ,idade, comendo =False,falando=False):
        self.nome = nome #seria igual p1.nome = 'Luiz'
        self.idade = idade
        self.comendo= comendo
        self.falando=falando


    def falar(self, assunto): #metodo é uma função dentro de uma classe
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return #parecido com o break nao vai executar oq vem posterior

            #varaivael 'global'                  variavel local 
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer(self,comida):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        
        print(f'{self.nome} está comendo {comida}')
        self.comendo= True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f"{self.nome} parou de comer")
        self.comendo = False

    def ano_nasc(self):
        return self.ano_atual - self.idade 

#Instanciar uma classe 
p1 = Pessoa('Caio',19)
p2 = Pessoa('Julia', 18)



try:
    p3 = Pessoa()
    print(p3.nome) #erro pois qunado eu instancio um p1 é diferente de p3.
except:
    print()
    print('testando os metodos e manipulando o objeto:\n') 
    p1.falar('POO')#chamamos o metodo assim
    p1.comer('pizza')
    p1.parar_falar()
    p1.comer('pizza')
    p1.falar('POO')
    p1.parar_falar()
    p1.parar_comer()
   

    print()
    print('Mostrando que objetos são idepedentes:\n') 
    p1.falar('POO')#chamamos o metodo assim
    p2.comer('potato')#chamamos o metodo assim
    print(f'{p1.nome} nasceu em : {p1.ano_nasc()}')
    print(f'{p2.nome} nasceu em : {p2.ano_nasc()}')

