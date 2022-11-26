""" 
    escopos - significa onde aquyele codigo pode atingir 
    escopo global - é onde todo codigo é alcançavel
    escopo local = onde apenas nomes do mesmo local podem ser alcançados
"""

x = 2
# definnindo um x global


def escopo():
    global x #mal pratica programação - transformando o x em global
    x =10
    # escopo local , impossivel manipular de fora 
    def outra_funcao():
        y = 2 
        print(x,y)

    outra_funcao()
    print(x)


print(x) # print em x global - seria 1 se mao tivesse o global
escopo()
print(x) # print em x global - variavel protegida outra variavel
