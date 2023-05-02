cont = 0
negativo = 0

while (cont < 4):
    n = int(input("informe um numero: "))

    if (n < 0):
        negativo = n
    cont = cont + 1

if (negativo < 0):
    print ("existe um numero negativo")
else:
    print ("nao existe um numero negativo")



