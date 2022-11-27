#Metodos uteis em dic
import copy

clientes= {
    'id' : 1,
    'nome':'Caio Zenke',
    'lista' : [0,1,2]
}

#len - conta quantas chaves
print('len:' , len(clientes))

# keys - mostra as chaves , fazer coersão pois retorna uma dict_keys
print('keys:' , list(clientes.keys()))

#values - retorna os valores
print('values :' ,list(clientes.values()))
print()
 
#items - retorna o chave e valor
for c,v in clientes.items():
    print(f'items chave/valor : {c},{v}')


#setdefault - seta o valor caso a chave nao exista

clientes.setdefault('idade',None)
print('setdefault idade:' , clientes['idade'])

#copy - afeta apenas os valoroes inmutaveis , deepcopy - copia profunda entra em valores mutaveis e subniveis
print()
c1 = clientes.copy()

c1['lista'][0] = 10000
print('afetou as duas com copy')
print(clientes)
print(c1)


print()
c1 = copy.deepcopy(clientes)
c1['lista'][0] = 1
print('uma nao afeta a outra com deepcopy - copia profunda')
print(clientes)
print(c1)


