#Faça um programa para imprimir:
"""    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""



#u = int(input('a'))

def ex1(n):
    num = u
    for i in range(n):
        print(n, end =' ')

#ex1(u)

"""Embaralha palavra.
Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
from random import *

def embaralha(s):
    embaralhar = sample(s,len(s))
    nl = embaralhar
    ns = ''.join(nl)
    return print(ns)    

#embaralha('python')






        

        