# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1

    for num in args:
        total *= num
    
    return total


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(num):
    
    par = num % 2 == 0

    if par:
        return f'{num} é par'
    return f'{num} é impar'


numero = multiplica(3,3)
print(par_impar(numero))



#Funções de Primeira classe

def saudacao(nome,msg):
    return f'{nome}, {msg}'


def executa_funcoes(funcao,*args):
    return funcao(*args)


print(executa_funcoes(saudacao,'caio','tudo bem?'))