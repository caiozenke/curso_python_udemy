
palavra_secreta = 'zenke'
palavra_usuario = []
nome = input("Digite seu nome: ")
chances = 3


while True:


    # Letra Digitada do Usuario e Verificação
    lu = input(f'{nome} , Digite uma Letra: ')
    letra_usuario = lu.lower()

    if len(letra_usuario) > 1:
        print('Safadinho Digite apenas uma letra!')
        continue


    #Adicionar ou nao a Letra do Usuario
    palavra_usuario.append(letra_usuario)

    if letra_usuario in palavra_secreta:
        print(f'A letra {lu} está na palavra!')
    else:
        palavra_usuario.pop()
        chances += -1
    print(f'{nome} tem {chances} chances!')



    #Loop para Adicionar letra na palavra mostrada para usuario
    palavra_temporaria = ''
    for letra in palavra_secreta:
        if letra in palavra_usuario:
            palavra_temporaria += letra
        else:
            palavra_temporaria += '_'




    #Verificação de Ganhar ou Perder
    if palavra_temporaria == palavra_secreta:
        print('')
        print(f'Parabens {nome} você ganhou! A palavra secreta era {palavra_secreta}')
        break
    else:
        print(f'A Palavra secreta está : {palavra_temporaria}')

    if chances == 0:
        print('')
        print (f'Você Perdeu!! A palavra secreta era {palavra_secreta}')
        break
