import sys
import time as t


#exewmplo 1

lista = [1,2,3,4,5]
lista = iter(lista)#transformar  em interador
print(next(lista))
print(hasattr(lista,'__name__')) #saber se a lista eh um interador




#exemplo 2 com geradores

#para diminuir o tamanho utilzado vc usa lista comprendidas 

l1=[x for x in range(1000)] # lista compreendida com 1000 valores
l2 = (x for x in range(1001)) #gerador com 1000 valores

print(sys.getsizeof(l1))#saber quanto de memoria esta lista esta ocupando 
print(sys.getsizeof(l2))# a diferença que a l2 é um gerador e vai te retornar um valor se vc pedir e apos isso ira guardar na memoria 

# acessamos os valores do gerador com next ou for
print(next(l2))

for v in l2:
    print(v , end=',')

def demora():         #funcao para criar simular um sistema demorado , para mostra o pq os geradores sao uteis
    r= []

    for v in range(121):
        r.append(v)
        t.sleep(0.2)
    return r 

d = demora()

#print(type(g))

for r in d:
    print(r)


def gerador(): #gerador 

    for v in range(121): #vai gerar um numero de cada vez
        yield v
        t.sleep(0.1)

g = gerador()

for n in g:
    print(n)
