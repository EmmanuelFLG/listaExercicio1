# O custo ao consumidor de um carro novo e a soma do custo de fabrica com a percentagem do distribuidor e dos impostos 
# (aplicados , primeiro os impostos sobre o custo de fabrica, e depois a percentagem do distribuidor sobre o resultado). 
# Supondo que a percentagem do distribuidor  seja de 28% e os impostos 45%. 
# Escrever um programa que leia o custo de fabrica de um carro e informe o custo ao consumidor do mesmo.

cFabri = float(input("Informe o custo de fabrica do carro:"))

impostos = cFabri * 45/100
valorImp = cFabri + impostos
percDistri = valorImp * 28/100
valorFinal = valorImp + percDistri

print ("o valor final e:", valorFinal)
