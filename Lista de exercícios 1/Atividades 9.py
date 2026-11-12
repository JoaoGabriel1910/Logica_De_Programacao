#9-	Crie um programa de adivinhação em que o computador escolhe aleatoriamente um número entre 1 e 50, e o usuário precisa adivinhar. O programa deve fornecer feedback (maior ou menor) a cada tentativa e permitir apenas 5 tentativas para acertar. Se o usuário acertar antes do limite, exiba uma mensagem de vitória; caso contrário, revele o número ao final.

import random

numero = random.randint(1,50)

for computador in range (5):
    num = int(input("Diite um valor: "))
    if num == numero:
        print("Acertou")
        break
    elif num > numero:
        print("Tente novamente, seu número é maior")
    elif num < numero:
        print("Teste novamente, seu número é menor")
    
if(erro == 1 ): 
    print ("O número sortiado foi: ", numero)