cont = 0
contPar = 0

while (cont < 4):
    n = int(input("informe um numero: "))
    cont = cont + 1

    if (n % 2 == 0):
        contPar = contPar + 1

print ("existem", contPar, "numeros pares")
        