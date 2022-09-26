#Aula sobre filter e reduce

from functools import reduce


produtos = [
    {'id' :'p1' , 'valor': 50},
    {'id' :'p2' , 'valor': 12.33},
    {'id' :'p3' , 'valor': 18},
    {'id' :'p4' , 'valor': 5.50},
    {'id' :'p5' , 'valor': 5},
    {'id' :'p6' , 'valor': 10},
    {'id' :'p7' , 'valor': 20},
    {'id' :'p8' , 'valor': 550.02},
    {'id' :'p9' , 'valor': 70},
    {'id' :'p10' , 'valor': 52.22},
]

pessoas = [
    {'nome': 'Caio' ,'idade': 18},
    {'nome': 'Joao' ,'idade': 8},
    {'nome': 'Pedro' ,'idade': 9},
    {'nome': 'AUGUSTO' ,'idade': 29},
    {'nome': 'Luan' ,'idade': 34},
    {'nome': 'José' ,'idade': 32},
    {'nome': 'Gustavo' ,'idade': 42},
    {'nome': 'maria' ,'idade': 43},
    {'nome': 'ana' ,'idade': 21},
 ]


#Exemplo 1 Filter - Pegar Produtos apenas maiores de 20

produtos_novos = filter(lambda p:p['valor'] > 20,produtos)
#com listas compreendidas
novos_produtos = [p for p in produtos if p['valor'] > 20]

for p in produtos_novos:
    print(p)


    
# REDUCE É COMO FOSSE UM ACUMALADOR, precisa passar um acumaldor , expressao , lista e valor inicial

#media dos preços dos produtos

media_produtos= reduce(lambda ac, p: round(p['valor'] + ac,2), produtos, 0 )

print()
print(f'A soma dos valores dos produtos foi de {media_produtos} e a media de {media_produtos / len(produtos)}')

#agora a media de idades das pessoas com apenas maiores de 18

pessoas_maiores = filter(lambda p: p['idade'] >= 18,pessoas)
lista = []

for p in pessoas_maiores:
    lista.append(p)
#print(lista)

media_pessoas = reduce(lambda ac, p : p['idade'] + ac, lista,0)
print(f'A média da idade das pessoas com maiores de 18 foi de : {int(media_pessoas / len(lista))} anos')
