#Somar o total com lista compreendidas

carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto1', 30))
carrinho.append(('Produto1', 30))
carrinho.append(('Produto1', 30))


# jeito tradicional
total=[]

for v in carrinho:
    total.append(v[1])

print(sum(total))


#metodo com lista compreendidaas

l1 = [(p,v) for p,v in carrinho]
l2 = [v for p,v in l1]
print(sum(l2))

#outra  tipos de resoluções 
l4=[v for p,v in carrinho]
print(sum(l4))

#ou
l3=sum([v for p,v in carrinho])
print(l3)