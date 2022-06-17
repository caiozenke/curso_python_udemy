#Calculadora simples

while True:
    print()
    #print pra pular linha

    x =input('Digite o Primeiro Número: ')
    y =input('Digite o Segundo Número: ')
    operador = input('Digite o Operador: ')

    if not x.isnumeric() or not y.isnumeric():
        print('Erro,Digite um Número')
        #Analisa se foi passado um numero

    x = int(x)
    y = int(y)


    #Calculos + , - , *

    if operador == '*':

        resolucao = x * y
        print(f'Resultado da multiplicação foi {resolucao}')

    elif operador == '-':
        resolucao = x - y
        print(f'Resultado  foi {resolucao}')

    elif operador == '+':
        resolucao = x + y
        print(f'Resultado da soma foi {resolucao}')
    else:
        print("Erro! Operador iNVALIDO")


    #Função Sair

    sair = input('Deseja sair? [s]im ou [n]ao: ')

    if sair == 's':
        print('Adeus')
        break