#7-	Crie um programa que solicite números ao usuário continuamente até que ele insira um número negativo. Em seguida, exiba a média dos números positivos fornecidos.


num = int(input("Digite um valor: "))
mediaNum = 0
contador = 0
numTotal = 0

while num > 0:
    if num > 0:
        contador += 1
        numTotal += num
        mediaNum = numTotal / contador
        num = int(input("Digite um valor: "))
print(mediaNum)