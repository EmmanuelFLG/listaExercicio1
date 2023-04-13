# Ler dois valores para as variaveis A e B, e efetuar as trocas dos valores de forma que a variavel A passe a possuir o valor 
# da variavel B e a variavel passe a possuir o valor da variavel A. Apresentar os valores trocados.

a = int(input("informe o valor de A:"))
b = int(input("informe o valor de B:"))

a2 = a
b2 = b

a = b2
b = a2

print ("valores de A e B trocados agora A vale:", a, "e B:", b)