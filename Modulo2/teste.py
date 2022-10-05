def lista_de_clientes(clientes,lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes)
    return lista
    
c1 = lista_de_clientes(['josé' , 'caio'])
c2 = lista_de_clientes(['Amanda','igor'])
print(c1)