# Faca um programa que receba um valor que foi depositado e exiba o valor com rendimento apos um mes. 
# Considere fixo o juro da poupanca em 0,50% a. m.

v = float(input("Informe o valor depositado:"))

rendM = (v * 0.50)/100
vtot = v + rendM

print ("Seu rendimento ao mes foi de:", rendM, "R$. Valor atual da conta:", vtot, "R$")