# Aulas sobre Set - São mutavaies porem so aceitam imutaveis no seu interno

#Criando set - com set()

s1 = set() #vazio
s1 =set('Caio') #Com dados , mas nao garante a ordem!

l1 = [1,2,2,2,2,3,3,4,2,4,5,6]

s2 = set(l1) #eliminam valores duplicados 
#print(s2)

#Metodos Uteis

s2.add('caio') #adiciona
s2.update(('caio'))#adicona de metodo iteravel- se for str vai iterar sobre ela
#s2.clear() limpa o set

#Exemplo de Uso

letras = set()

while True:
    
    letra = input('Digite Uma Letra:')
    
    letras.add(letra)

    if 'c' in letras:
        print('achou a letra')
        break
    
    print(letras)
