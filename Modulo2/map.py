#mapear dados
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
    {'nome': 'Joao' ,'idade': 20},
    {'nome': 'Pedro' ,'idade': 22},
    {'nome': 'AUGUSTO' ,'idade': 29},
    {'nome': 'Luan' ,'idade': 34},
    {'nome': 'José' ,'idade': 32},
    {'nome': 'Gustavo' ,'idade': 42},
    {'nome': 'maria' ,'idade': 43},
    {'nome': 'ana' ,'idade': 21},
 ]


l1= [1,2,3,4,5,6,7,8,9,10]

#exemplo 1
def multi(lista):
    return lista * 2

            #obrigatorio passar uma func como primeiro
teste = map(multi,l1)

print(list(teste))

#exemplo 2 - Aumentar o Preço em 10 por cento

def aumenta(p):
    p['valor'] = round(p['valor'] * 1.05)
    return p

map_valor = map(aumenta,produtos)

for np in map_valor:
    print(np)
    
print()   
#exemplo 3 pegar os nomes das pessoas

nomes = map(lambda nome:nome['nome'], pessoas)


for n in nomes:
    print(n)
