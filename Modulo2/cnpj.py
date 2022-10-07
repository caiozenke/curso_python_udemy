"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import re

def remover_caracter(cnpj):
    carac = re.sub(r'[^0-9]','',cnpj)
    return carac


def primeiro_digito(numeros):
    cnpj = numeros[:-2]
    lcnpj =[]
    lmult =[]
    num = 6
    for n in cnpj:
        num += -1
        if num == 1:
            num = 9
        num_cnpj =int(n)
        lmult.append(num)
        lcnpj.append(num_cnpj)
                
    total =sum([(x*y) for x,y in zip(lcnpj,lmult)])
    formula =11 - (total % 11)
    
    if formula > 9 :
        formula = 0
    
    return cnpj + str(formula)


def segundo_digito(cnpj):
    lcnpj =[]
    lmult =[]
    num = 7
    for n in cnpj:
        num += -1
        if num == 1:
            num = 9
        num_cnpj =int(n)
        lmult.append(num)
        lcnpj.append(num_cnpj)
                
    total =sum([(x*y) for x,y in zip(lcnpj,lmult)])
    formula =11 - (total % 11)
    
    if formula > 9 :
        formula = 0
    
    return cnpj + str(formula)


def verifica(original,cnpj):
    if original == cnpj:
        return('CNPJ Valido!')
    else:
        return('CNPJ INVALIDO')
        

#Testes
  
usuario = input('Digite Um CNPJ:')

cn = remover_caracter((usuario)) 
t1 = primeiro_digito(cn)
t2 = segundo_digito(t1)

variavel = verifica(cn,t2)
print(usuario ,'-', variavel)



    