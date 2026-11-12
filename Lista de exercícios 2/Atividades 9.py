nome = input("Digite o nome do cliente : ")
valorCompra = int(input("Digite o valor da compra que você realizou no ano passado : "))
valorFinal = 0

if valorCompra < 500000 :
    valorFinal = valorCompra * 0.9
    print(valorFinal)
elif valorCompra > 500000 :
    valorFinal = valorCompra * 0.85
    print(valorFinal)