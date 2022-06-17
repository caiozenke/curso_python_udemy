"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num =input('Digite um número inteiro: ')


if not num.isdigit():
    print(f'ERRO! {num} não é inteiro!')
else:
    num = int(num)
    if num % 2 == 0:
        print(f'O Número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')


