idade = input('Digite uma idade:')



if not idade.isnumeric():
    print("Digite Um Número Inteiro")
else:
    idade = int(idade)
    maior_idade = idade >= 18
    msg = (f"Você tem {idade},Acesso Liberado!") if maior_idade else 'Não pode Acessar'

    print(msg)

#jeito errado

if idade >= 18:
    idade = True
else:
    idade = False