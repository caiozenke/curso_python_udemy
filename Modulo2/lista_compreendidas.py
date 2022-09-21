#lista comprehension serve para otimizar (menos linhas)


l1 =[1,2,3]
l2= [n for n in l1] #vai jogar a lista dentro desta

#multiplicar por dois
exemplo = [ v*2 for v in l1] 
print('exemplo' , exemplo)

#coordenadas
exemplo_1 =[(x,y) for x in l1  for y in range(0,6)]
print('exemplos 1',exemplo_1)

#tuplas inverter
tupla = (
    ('chave 1', 'valor1'),
    ('chave 2', 'valor2'),
)

ex_2 =[(v,c) for c,v in tupla] 
d = dict(ex_2)
print('exemplo tuplas invertidas:',d)


#trocar algo no nome

ln = ['Caio', 'Felipe', 'André', 'Songela']

trocar_ln = [v.replace('a', '0').upper() for v in ln]
print('exemplo troca de algo no nome:', trocar_ln) 



#filtar listas

lnum = list(range(51))

filtro = [n for n in lnum if n % 5== 0 or n % 7==0]
print('exemplo divisives 5 e 7',filtro)





#loucura releva
'''def teste(lista ,lista2):
    a = 0

    for v in lista:
       for v2 in lista2:
           if v == v2:
               a = print('numero duplicado!')
               break
    return a


var = teste(l1,l2)
print(var)'''