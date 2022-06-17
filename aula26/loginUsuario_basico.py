usua_nome = input('Digite o Nome Do Usuario: ')
usua_senha=input('Digite a Senha do Usuario: ')


usua_db= 'Caio Zenke'
senha_bd = 'Caio1234'

if usua_db == usua_nome and senha_bd == usua_senha:
    print('Usuario Logado!')
else:
    print('Login Invalido.')