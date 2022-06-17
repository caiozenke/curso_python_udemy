nome = 'Caio Zenke' #str
idade = 18 #int
altura =1.79 #float
e_maior= idade > 18 #bool
peso = 68 #int
imc= peso / ( altura **2 )

print(f'{nome} tem {idade} anos de idade  e seu imc é {imc:.2f}')
                                                       #:2f irá mostra apenas 2 numeros depois do ponto

#com format agora
print('{} tem {} anos de idade  e seu imc é {}'.format(nome,idade,imc))
print('{0} tem {2} anos de idade  e seu imc é {1}'.format(nome,idade,imc))
print('{n} tem {i} anos de idade  e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))