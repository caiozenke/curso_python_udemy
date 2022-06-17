#Exercicio


nome =str (input('Digite seu Nome:'))
idade=int (input('Digite sua idade:'))
peso =float (input('Digite seu peso:'))
altura  =float (input('Digite sua altura :'))
ano= 2022
imc= peso / ( altura **2 )
data_nasc = ano - idade

print(f'{nome}  sua idade é {idade} , nascido no ano de {data_nasc}, com altura {altura} , peso {peso} e o imc de {imc:.2f}')




