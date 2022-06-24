l1 = [0,2,3,4,5,6,7,8,9,10]
l2 = ['str',1, True, 20.5]

soma= 0


#soma da valores
for valor in l1:
    soma += valor
    print(f'{soma} + {valor} = {soma}')


#tipos de elementos
print()

for tipo in l2:
    print(f'o tipo do elemento {tipo} é {type(tipo)}')