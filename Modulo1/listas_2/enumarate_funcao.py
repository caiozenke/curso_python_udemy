#enumera as listas em python como indices


lista1 = ['Caio', 'Luan', 'Zenke']
conta = 1

for indi,nome in enumerate(lista1):
    conta += indi
    if conta > 3:
        conta += -1
    print(f'o {conta} nome é {nome}')