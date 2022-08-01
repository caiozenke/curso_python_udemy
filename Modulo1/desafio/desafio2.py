
"""
Validação de um cpf
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

cpf = '16899535009'
novo_cpf = cpf[:-2]     #eliminando os ultimos dois valores do cpf
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



# Tirei do loop pois analisava o cpf da primeira vez do loop
teste = novo_cpf
msg = "CPF Valido" if cpf == novo_cpf else 'CPF INVALIDO'
print(teste, '-',msg)