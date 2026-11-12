#8-	Peça ao usuário um número inteiro positivo e exiba todos os números pares de forma decrescente até chegar a zero. O programa deve exibir a sequência de forma organizada, considerando que o número de entrada pode ser par ou ímpar.

num = int(input("Digite um valor: "))

if num % 2 == 0:
    for contador in range (num, -1, -2):
        print(contador)
else:
    for contador in range (num - 1, -1, -2):
        print(contador)