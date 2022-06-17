num= input('Digite um Numero: ')
num1 = input('Digite outro Numero:')

if num.isdigit() and num1.isdigit():
    #Verificar se o usuario digitou algo!

    soma = float(num) + float(num1)

    print('A soma dos números é {s:.2f}.'.format(s=soma))
else:
    print('Erro ao Converter os Números')
