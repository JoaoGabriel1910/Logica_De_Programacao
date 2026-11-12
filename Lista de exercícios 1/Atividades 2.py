#2-	Fazer um programa que calcule a tabuada de qualquer número, e o limite de cálculo deve ser definido pelo usuário:

numTabuada = int(input("Digite que tabuada você quer: "))
limite = int(input("Digite até que número deseja que a tabuada multipique: "))

for tabuada in range (0, limite + 1):
    multiplicacao = numTabuada * tabuada
    print(multiplicacao)