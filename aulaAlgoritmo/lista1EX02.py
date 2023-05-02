n1 = int(input("informe o primeiro numero: "))
n2 = int(input("informe o segundo numero: "))
n3 = int(input("informe o terceiro numero: "))

maior = 0
menor = 9999

if (n1 > maior):
    maior = n1

if (n2 > maior):
    maior = n2

if (n3 > maior):
    maior = n3


if (n1 < menor):
    menor = n1

if (n2 < menor):
    menor = n2

if (n3 < menor):
    menor = n3

if (n1 == n2 and n1 == n3):
    print ("os tres numeros são iguais")
else:
    print ("os numeros sao diferentes")


print ("maior numero: ", maior)

print ("menor numero: ", menor)