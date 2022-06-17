"""
Entrada de Dados

"""

#nome = input('Qual seu nome? ')
#print(f'O usuario digitou {nome} e o tipo da variavel é ' f'{type(nome)}')

nome = input("Digite seu nome:")
idade = input('Digite sua Idade')

data_nasc = 2021 - int(idade)

print(f'Data de Nascimento é {data_nasc}', end= ',')
print('Idade: {i} , seu nome é {n} '.format(i=idade, n=nome))
