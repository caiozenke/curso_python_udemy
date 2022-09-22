"""
Criando a tabela pro campeonato do bairro.
 
"""
from itertools import permutations as permu
from time import sleep
print()


def bairro():
    lista_times =[]
    
    while True:

        qtd_times= input('Digite quantos Times irão Jogar: ')
        
    
        if qtd_times.isnumeric():
            qtd = int(qtd_times)
            break
        else:
            print('Digite Números Inteiros,please!') 
    

    sleep(0.1)        
    print()   
    for c in range(qtd):
        
        lista_times.append(input(f'Digite o  nome do {c + 1} time: '))
    print('\nGerando a sua tabela...\n')
    sleep(2.0)
    
    
    for t in permu(lista_times,2):
        print(f'Jogo: {t[0]} vs {t[1]}')
            
            
print('-'*40)
print(' Monte a tabela pro campeonato do bairro.'.center(20))
print('-'*40)
print()
bairro()
