# Elaborar um programa que efetue a apresentacao do valor da conversao em real (R$) de um valor lido em dolar (US$).
# O programa devera solicitar o valor da cotacao do dolar e a quantidade de dolares disponiveis com o usuario.

cotD = float(input("informe a cotacao atual do dolar:"))
real = float(input("informe o valor em Real que deseja converter para dolar:"))

conv = real / cotD

print ("voce tera ",round(conv, 2), "US$" )
