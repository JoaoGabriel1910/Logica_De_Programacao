#3-	Fazer um programa que retorne quantos valores digitados pelo usuário são negativos. Repetir o enquanto até o usuário digitar o valor ZERO:

numRepeticao = int(input("Digite 0 se quiser continuar e qualquer outro para parar: "))
num = int(input("Digite um número"))
qtdValores = 0

#if numeRepeticao == 0

while num != 0:
    if num < 0:
        qtdValores += 1
    num = int(input("Digite um número (ou 0 para parar) "))
print("A quantidade de valores é: ", qtdValores )