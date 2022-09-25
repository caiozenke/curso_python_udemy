
from itertools import groupby,tee


jogadores = [
    {'nome': 'Caio' ,'Tier': 'A'},
    {'nome': 'Joao' ,'Tier': 'B'},
    {'nome': 'Pedro' ,'Tier': 'A'},
    {'nome': 'AUGUSTO' ,'Tier': 'B'},
    {'nome': 'Luan' ,'Tier': 'C'},
    {'nome': 'José' ,'Tier': 'B'},
    {'nome': 'Gustavo' ,'Tier': 'D'},
    {'nome': 'maria' ,'Tier': 'E'},
    {'nome': 'ana' ,'Tier': 'A'},
    {'nome': 'Nicolas' ,'Tier': 'C'},
    {'nome': 'Andre' ,'Tier': 'B'},
    {'nome': 'Lucas' ,'Tier': 'C'},
    {'nome': 'Lipe' ,'Tier': 'D'},
    {'nome': 'EDU' ,'Tier': 'E'},
]

#obrigatorio ordernar os valores

ordenar = lambda item:item['Tier']
jogadores.sort(key=ordenar)
j_agrupa = groupby(jogadores,ordenar)


for t,j in j_agrupa:
    cop1, cop2= tee(j) #copiar para nao esgotar o interador
    print(f'Agrupamento {t}:')

    for n in cop2:
        print(f'\t{n}')
    
    print(f'\tSão {len(list(cop1))} jogadores Tier {t}')

    print()

    
   


