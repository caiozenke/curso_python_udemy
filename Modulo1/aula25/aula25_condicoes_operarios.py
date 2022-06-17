"""     If/Else/Elif com operadores Relacionais
        ==  >= >   <  <=  =!
"""


nome =input('Digite seu nome: ')
idade = int(input('Digite Sua Idade: '))

#Emprestimos Condições

idade_menor = 18   #idade minima para solicitar emprestimo.

idade_maior = 30   #idade maxima para solicitar o emprestimo.

if idade >= idade_menor and idade <=idade_maior:

    print(f'{nome} está apto a receber o emprestimo.')
else:
    print(f'{nome} Não está apto para receber o emprestimo.')





# Outro jeito De ser Resolvido

"""if idade >= 18 and idade <= 30:

    print(f'{nome} está apto a receber o emprestimo.')
else:
    print(f'{nome}Não está apto para receber o emprestimo.')"""