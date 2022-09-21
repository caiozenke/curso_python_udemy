# funcao normal

def func(argumento,arg2):
    return argumento * arg2

var = func(2,5)
print(var)


#funcao anonima e ou lambda

v= lambda num1,num2 : num1* num2

#print(v(9,2))

lista =[
    ['P1', 10],
    ['P2', 2],
    ['P3', 8],
    ['P4', 5],
    ['P5', 4],
    ['P6', 12],
]


"""def ordernar(produto):
    return produto[1] """
#lista.sort(key=lambda item: item[1] ,reverse=True) #ordenada com função lambda

print(sorted(lista, key=lambda produto: produto[0], reverse=True)) #ordena por maior ao menor
'''
for produto in lista:
    print(f'produto {produto[0]} valor: {produto[1]}')
    '''