cont = 0

c = int(input("informe a capacidade do elevador: "))

while (cont < 4):
    n = int(input("informe o peso:"))

    if (cont > 0):
        peso = peso + n
        cont = cont + 1
    
    if (cont == 0):
        peso = n
        cont = cont + 1

        
print ("a soma dos pesos foi:", peso)

if (n > c):
    print ("capacidade excedida")
else:
    print ("esta dentro da capacidade")

