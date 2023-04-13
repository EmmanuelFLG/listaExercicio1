# Escrever um programa que leia o nome de um vendedor, o seu salario fixo e o total de vendas efetuadas por ele no mes (em dinheiro). 
# Sabendo que este vendedor ganha 15% de comissao sobre suas vendas efetuadas, 
# informar o seu nome, o salario fixo e salario no final do mes.

nome = input("Infome seu nome:")
sFixo = float(input("informe seu salario fixo:"))
totVendas = float(input("informe em reais o ganho do total de vendas feitas no mes:"))\

comi = totVendas * 15/100

sFinal = sFixo + comi

print ("Nome:", nome, "Salario fixo:", sFixo, "Salario final:", sFinal)






