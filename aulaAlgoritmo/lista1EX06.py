cont = 0
contImpar = 0

while (cont < 4):
    n = int(input("informe um numero: "))
    cont = cont + 1

    if (n % 2 == 1):
        contImpar = contImpar + 1

print ("existem", contImpar, "numeros impares")