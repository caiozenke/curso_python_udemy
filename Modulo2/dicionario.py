import copy

#aula sobre dicionario


      #chave  : valor da chave
d1 = {'TopLaner': 'Sett'}
d1 ['nova chave'] = {'novo valor'}


#criar com a função dict

d2 =dict(chave1 = 'new key')

#acessar um valor de uma chave
'''print(f'valor da chave 1: {d2["chave1"]}')
print(d1['TopLaner'])'''


#utlizar apenas valores imutaveis ou strgs


d3 ={
    'string':'valor da strg',
    123:321,
    (0,1,2):'tuplas'
}

'''teste = input('Achar na Tupla:')

if d3.get(teste) is not None:
    print(d3[teste])
else:
    chave = input('Digite A chave nova')
    valor = input('digite o valor da chave')
    d3.update({chave:valor})  #adiciona na tupla

print(d3[teste])

'''
#acessar os valores e chaves da tupla 
'''for v in d3.values():
    print(v)


print('string' in d3.keys())

for v in d3.keys():
    print(v)'''



#Exemplo real


pacientes ={
    'Paciente1' : {
        'Nome' : 'Caio',
        'Sobrenome' : 'Zenke',
        'Email' :  'caiolzenke@gmail.com',
    },
    'Paciente2' : {
        'Nome' : 'Felipe',
        'Sobrenome' : 'Zenke',
        'Email' :  '321zenke@gmail.com',
    }
}

#PARA VER AS CHAVES E VALORES DELA USAMOS O ITEMS()

for paci_k , paci_v in pacientes.items(): #Primeira INteração do Loop
    print(f'Exibindo: {paci_k}')
    for dados_k , dados_v in paci_v.items(): #Segunda Interação para acessar os dados dentro do valor que é um dict
       print(f'\t{dados_k} : {dados_v}')  # \t é tipo um tab no print





# copiar um dicionario usamos o modulo copy
'''
c = copy.deepcopy(pacientes)
c['Paciente2'][2]='casodiapos@gmail.com'
print(c)'''


#concatenar TUplas usamos o update inves do +
'''
letras1={
    'a': 1,
    'b': 2,
    'c': 3,
}

letras2= {
    'd':4,
    'e':5,
    'f':6,
}
print(f'dicionario1 :{letras1}')
print(f'dicionario2 :{letras2}')

letras1.update(letras2)

print(f'concatenado:{letras1}')'''