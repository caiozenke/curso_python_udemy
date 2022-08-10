"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def func1(args):
    print(args)

def func2():
    v2 = 'Valor da func2'
    return  v2

vaa = func2()

func1(f'func1 recebeu o {vaa}')