"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Digite o Horario: ')

if not  horario.isdigit():
    print(f'Não {horario}é Valido')
else:
    horario=int(horario)

    if horario < 12 :
        print(f'São {horario} horas, Bom dia !!!!')

    elif horario >= 12 and  horario < 18:
        print(f'São {horario} horas , Bom Tarde !!!!')

    else:
        print(f'São {horario} horas , Bom Noite !!!!')
