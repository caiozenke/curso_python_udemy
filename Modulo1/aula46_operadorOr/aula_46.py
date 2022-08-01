# or ajuda na diminuição de ifs
#sempre vai retoranr o primeiro valor True , Ex: False or True , retorna o True

nome = input('Digite seu nome:')

"""Sempre vai retorar o primeiro valor True , 
                            no caso se for um Nome a variavel nome é true ou se Nome nao for nada a frase Vira True  """
nomebonito = 'Nome Bonito' if nome == 'Caio' else nome or 'Você nao digitou nada'
print(nomebonito)