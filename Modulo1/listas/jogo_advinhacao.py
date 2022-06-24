
palavra_secreta = 'matue'
palavra_usuario = []


while True:

    lu = input('Digite uma Letra: ')
    letra_usuario = lu.lower()

    if len(letra_usuario) > 1:
        print('Safadinho Digite apenas uma letra!')
        continue


    palavra_usuario.append(letra_usuario)
    if letra_usuario in palavra_secreta:

        print(f'A letra {lu} está na palavra!')
    else:
        print(f'A letra {lu} não está na palavra!')
        palavra_usuario.pop()


    palavra_temporaria = ''
    for letra in palavra_secreta:

        if letra in letra_usuario:
            palavra_temporaria = palavra_temporaria + letra

        else:
            palavra_temporaria += '_'

    print(palavra_temporaria)