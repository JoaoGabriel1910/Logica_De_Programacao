codigo = 1
alimentoNaoPerecivel = 0
alimentoPerecivel = 0
vestuario = 0
higienePessoal = 0 
limpeza = 0
produtoNaoIndentificado = 0


while codigo != 0:
    codigo = int(input("Digite o CÓDIGO: "))
    if codigo == 1: 

        alimentoNaoPerecivel += 1 
    elif codigo <= 4:
        alimentoPerecivel += 1
    elif codigo <= 6:
        vestuario += 1
    elif codigo == 7:
        higienePessoal += 1
    elif codigo <= 15:
        limpeza += 1
    else: 
        print ("ERRO")


print("Quantidade de alimento não percecível", alimentoNaoPerecivel, "\nQuantidade de alimentos perecíveis", alimentoPerecivel, "\n Quantidade de vestuário", vestuario, "\nQuantidade de limpeza e utensílios domésticos", limpeza, "Quantidade de higiene pessoal", higienePessoal)

