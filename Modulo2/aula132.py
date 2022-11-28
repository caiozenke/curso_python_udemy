#função lambda

# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]



# usamos sorted para ordernar e passamos uma key sendo func
def ordernar(item):
    return item['sobrenome']


l1 = sorted(lista , key= lambda item: item['nome'])# passamos a funcao em uma linha com a lambda 
l2 = sorted(lista, key= ordernar)


for item in l2: print(item)

print()
for item in l1:
    print(item)
    

