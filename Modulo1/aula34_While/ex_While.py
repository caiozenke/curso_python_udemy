"""

While Exercicios Basicos

"""
""" 
while True: #loop Infinito
      #Condição
    nome = input('qual seu nome?')
    print(f'seu nome é {nome}')
"""

x = 0 #coluna


while x < 10:

    y = 0  # linha
    x += 1
    while y < 5:
        y += 1
        print(f' ( Coluna={x}, Linha={y})')

print('acabou')