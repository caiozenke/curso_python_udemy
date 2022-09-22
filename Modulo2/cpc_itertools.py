"""
Combinations, Permutation e Product - Itertools

Combinação - Ordem nao importa
Permutação - ordem importa
Ambos nao reptete valor
Produto - ordem importa e repete valores
"""
from itertools import combinations,permutations,product, repeat

lista = ['Joinvile' , 'Vasco' , 'José']

#combinações com combinations
                        #grupos de quantos
for t in combinations(lista,2):
    print(t)
    """ saida ↓
    ('Joinvile', 'Vasco')
    ('Joinvile', 'José')
    ('Vasco', 'José')
    """
    
    
#combinações com permutacions 
for v in permutations(lista,2):
    print(v)
    """ saida ↓
    ('Joinvile', 'Vasco')
    ('Joinvile', 'José')
    ('Vasco', 'Joinvile')
    ('Vasco', 'José')
    ('José', 'Joinvile')
    ('José', 'Vasco')
"""



#combinações com product

for p in product(lista,repeat=3):
    print(p)
    """ saida ↓ vai retornar todas combinações com repetição de um
    ('Joinvile', 'Vasco')
    ('Joinvile', 'José')
    ('Vasco', 'José')
    ('Joinvile', 'Joinvile', 'Joinvile')
    ('Joinvile', 'Joinvile', 'Vasco')
    ('Joinvile', 'Joinvile', 'José')
    ('Joinvile', 'Vasco', 'Joinvile')
    ('Joinvile', 'Vasco', 'Vasco')
    ('Joinvile', 'Vasco', 'José')
    ('Joinvile', 'José', 'Joinvile')
    ('Joinvile', 'José', 'Vasco')
    ('Joinvile', 'José', 'José')
    ('Vasco', 'Joinvile', 'Joinvile')
    ('Vasco', 'Joinvile', 'Vasco')
    ('Vasco', 'Joinvile', 'José')
    ('Vasco', 'Vasco', 'Joinvile')
    ('Vasco', 'Vasco', 'Vasco')
    ('Vasco', 'Vasco', 'José')
    ('Vasco', 'José', 'Joinvile')
    ('Vasco', 'José', 'Vasco')
    ('Vasco', 'José', 'José')
    ('José', 'Joinvile', 'Joinvile')
    ('José', 'Joinvile', 'Vasco')
    ('José', 'Joinvile', 'José')
    ('José', 'Vasco', 'Joinvile')
    ('José', 'Vasco', 'Vasco')
    ('José', 'Vasco', 'José')
    ('José', 'José', 'Joinvile')
    ('José', 'José', 'Vasco')
    ('José', 'José', 'José')
    """