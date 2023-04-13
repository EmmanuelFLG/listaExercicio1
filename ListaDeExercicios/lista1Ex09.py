# Faca um programa que leia a idade de uma pessoa expressa em anos,  
# meses e dias e mostre-a expressa apenas em dias, suponha todos os meses com 30 dias.

anos = int(input("informe quantos anos voce tem:"))
meses = int(input("informe os meses:"))
dias = int(input("informe os dias:"))

anoMes = anos * 12 
mesDia = (meses + anoMes) * 30
diasTot = mesDia + dias

print ("Sua idade em dias e:", diasTot)