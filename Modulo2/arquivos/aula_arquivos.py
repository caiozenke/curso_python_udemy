# +w possibilita arquivo a ler e escrever mas apaga se for escrever denovo
# r apenas leitura
# a+ escreve e  apaga (append)
arq = open('abc.txt','w+')

teste = input('digite')
arq.write('Caio\n') #Write escrever no Arquivo
arq.write('Luan\n') #Write escrever no Arquivo
arq.write('Luan\n') #Write escrever no Arquivo

arq.seek(0,0) # a funcao ira ir ate o final do arquivo e voltar para o inicio,assim irá lr o arquivo
print(arq.read()) #para nao ler o arquivo em branco usamos o seek, pois nao foi 'commitado' as linhas

print('#################')
print( )

arq.seek(0,0) #jogando o cursor para o começo novamente
print(arq.readlines()) #retorna uma lista

print('#################')
print( )

arq.seek(0,0) #jogando o cursor para o começo novamente
for linha in arq:
    print(linha , end='')


arq.close()#sempre fechar os arquivos ,como um commit
print()
print('#################')
print()

#exemplo com try e finally

try:
    arq = open('tryefinaly.txt', '+w')
    arq.write('heelo word')
    arq.seek(0)
    print(arq.read())
finally: #Usamos o Finally pois qualquer erro o arquivo mesmo assim sera fechado
    arq.close()

print()
print('#################')
print()


#exemplo mais pytista com o with
with open('teste.txt' ,'a+') as arq: #Vantagem qeu nao precisa fechar o arquivo
    arq.write(f'{teste} \n')

    arq.seek(0)
    print(arq.read())