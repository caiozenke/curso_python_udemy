# gerar um cpf

from random import randint

cpf = str(randint(100000000,999999999))
novo_cpf = cpf     #eliminando os ultimos dois valores do cpf
multiplo = 10
total = 0

for index in range(19):
    if index > 8:       # Primeiro índice vai de 0 a 9,
        index -= 9      # São os 9 primeiros digitos do CPF


    total += int(novo_cpf[index]) * multiplo # Valor total da multiplicação

    multiplo -= 1 # Decrementa o contador reverso

    if multiplo <2:
        multiplo = 11

        d = 11 -(total % 11)

        if d > 9:
            d = 0  # Se o digito for > que 9 o valor é 0
        total = 0
        novo_cpf += str(d) # Adiciona ao novo cpf

print(f'Cpf: {novo_cpf}')