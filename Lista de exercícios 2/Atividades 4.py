j1 = 0
j2 = 0
while True:
    ponto = int(input("Qual jogador fez o ponto?\n1- jogador 1\n2 - jogador 2\n"))
    if ponto == 1:
        j1 += 1
    elif ponto == 2:
        j2 += 2
    else:
        print("Opção invalida")
        continue
    print("---PLACAR---\njogador 1:" , j1 , "  jogador 2:" , j2 , "\n")
    if j1 >= 21 and (j1 - j2) >= 2:
        print("Jogador 1 venceu a partida!")
        break
    elif j2 >= 21 and (j2 - j1) >= 2:
        print("Jogador 2 venceu a partida!")
        break
