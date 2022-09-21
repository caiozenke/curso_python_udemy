# separar a str= 01234567890123456789012345678901234567890123456789012345678901234567890123456789 em seu padrao
#depois separar 0123456789.0123456789.0123456789



str = '0123456789012345678901234567890123456789'
novo = '.'
pular_numeros = input("digite um numero que irá pular")
pular =int(pular_numeros)

                        #fatiar em quantos      for com range
lista = novo.join([str[numero:numero +pular] for numero in range(0,len(str), pular)])
print(lista)