#6-	Peça ao usuário para fornecer um número inicial e um intervalo. Em seguida, faça uma contagem regressiva do número inicial até zero, decrementando pelo intervalo especificado.

numIni = int(input("Insira o número em que irá começar: "))
intervalo = int(input("Insira o intervalo: "))

for contador in range (numIni, -1, -intervalo):
    print(contador)