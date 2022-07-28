
"""
For estrutura

"""

texto = input('Digite um texto: ')

novo_texto = ''
for n ,letra in enumerate(texto):

    if letra == 'c':
        novo_texto += letra.upper()
    else:
        novo_texto += letra

    print(f'{n}: {novo_texto}')




"""
print('Multiplos de 5')

        #    start/pare/pule
for n in range(0, 101 , 5):
        print(n, end=' , ')

#ou

print()
print('Multiplos de 8')
for n in range(100):
    if n % 8 == 0:
        print(n, end=' , ')
"""