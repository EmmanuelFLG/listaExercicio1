n = int(input("informe o numero de gols do time da casa: "))
n2 = int(input("informe o numero de gols do time visitante: "))

if (n == n2):
    print ("empate")

if (n > n2):
    print ("vitoria do time da casa")

if (n < n2):
    print ("vitoria do time visitante")