# Dado um numero  inteiro, positivo, menor do que 1000 obter a quantidade de centenas, dezenas e unidades desse numero. 
# Exemplo: dado o n° 764, obter Centena = 7, Dezena = 6 e Unidade = 4.

n = int(input("informe o numero (menor do que 1000):"))


while (n >= 1000):
    print ("o numero informado deve ser menor que 1000 tente novamente")
    n = int(input("informe o numero (menor do que 1000):"))

cent = n//100
restCent = n%100
dez = restCent//10
uni = restCent%10


print (cent)
print (dez)
print (uni)
