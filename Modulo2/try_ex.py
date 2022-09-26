#testando try


def divide(n1,n2):
    return n1/n2

log_erros =[]
count_erro = 0
while count_erro < 3:
    
    num1 = float(input('Digite o dividendo: '))
    num2 = float(input('Digite o divisor: '))
    print()

    try:
            divide(num1, num2)
    except ZeroDivisionError as error:
            print('Impossivel Dividir por 0')
            log_erros.append(error)
            count_erro += 1

print()
print('Esgotou os Erros! Foram Estes Erros')
for e in log_erros:
    print(e)