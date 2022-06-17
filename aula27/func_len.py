#LEN NAPO FUNCIONA COM NUMEROS,FLOATS E BOO
nome= input('Digite o nome do usuario: ')
senha= input('Digite a senha do usuario: ')

qtde_caracter = (senha.__len__()) # ou len(senha)

if qtde_caracter > 5:
    print('Cadastrado no Sistema!')

else:
    print('Erro! Senha muito curta!')