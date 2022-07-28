"""
SPLIT = Vai dividir uma str e transformar em lista
Vai Dividir em Dois Indices
"""


teste = 'This is Elon Musk , Ceo of Tesla'
print(teste)
print('')

#lista 0
print('lista 0')
lista = teste.split(' ')
print(lista)

for palavra in lista:
    print(palavra)


#lista 1

print('')
print("Lista 1")
lista1 = teste.split(',')
print(lista1)

for palavra in lista1:
    print(f'Palavra : {palavra} ; Apareceu{lista1.count(palavra)}')



