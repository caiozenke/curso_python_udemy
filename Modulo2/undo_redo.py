

from time import sleep


lista_tarefas = []

while True:
    print()
    print('-----Adicionador Tarefas-----')
    print('     1 - Adicionar Tarefa    ')
    print('     2 - Remover Tarefa      ')
    print('     3 - Mostrar Tarefa      ')
    print('     4 - Sair                ')
    print('-----------------------------\n')
    
    
    sleep(0.5)
    clique = input('O que deseja Fazer?')
    
    if clique.isnumeric():
        clique = int(clique)
    else:
        print('Digite Um número seu safado!')
    
    if clique == 1:
        tarefa =input('Digite Uma Tarefa: ')
        lista_tarefas.append(tarefa)
        print(f'A Tarefa {tarefa} foi adicionada\n')
        sleep(0.5)
        
    elif clique == 2:
        try:
            lista_tarefas.pop()
            print(f'{tarefa} foi excluida')
            sleep(0.5)
        except IndexError as error:
            print(f'Não é Possivel excluir algo que nao existe \n\t Error --> {error} <--')
            sleep(0.5)
            
    elif clique == 3:
        print(f'A lista Está assim {lista_tarefas}')
        
        sleep(0.5)
        
    elif clique == 4:
        break
    