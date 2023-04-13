# Faca um programa que receba o preco de custo de um produto e mostre o valor de venda. 
# Sabe-se que o preco de custo recebera um acrescimo de acordo com um percentual informado pelo usuario.

pCust = float(input("Informe o valor de custo do produto:"))
perc = int(input("Informe o percentual para o acrescimo no preco de custo do produto:"))

vAcresc = pCust * perc/100

vFinal = pCust + vAcresc

print("o valor acrescido sobre o produto foi de:", vAcresc, "Valor final do produto:", vFinal)
