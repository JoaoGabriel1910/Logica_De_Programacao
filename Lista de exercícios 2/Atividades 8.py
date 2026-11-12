valorCarro = 0
PagamentoParcelado = 0
PagamentoAVista = 1.20
metodoDePagamento = 0
valorFinal = 0
parcelas = 0 

valorCarro = float(input("Digite o valor do carro: "))
metodoDePagamento = float(input("Inira o metodo de pagemnto se vai querer:\n 1 - Pagar a vista 2 - Pagamento parcelado :"))

if  metodoDePagamento == 1:
    PagamentoAVista = valorCarro * 0.80
    print (PagamentoAVista)

elif metodoDePagamento == 2:
    PagamentoParcelado = int(input("Gostaria de parcelar em quantas vezes? \nOpções de: \n1- 6x : \n 2- 12x :  \n3- 18x : \n4- 24x :  \n5- 30x :  \n 6- 36x :  \n7- 42x :  \n 8 - 48x :  \n 9 = 54x :  \n10 -60x : \n : "))
    
    if PagamentoParcelado == 6:
        valorFinal = valorCarro * 1.03
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 12:
        valorFinal =valorCarro * 1.06
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 18:
        valorFinal =valorCarro * 1.09
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 24:
        valorFinal =valorCarro * 1.12
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 30:
        valorFinal =valorCarro * 1.15
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 36:
        valorFinal =valorCarro * 1.18
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 42:
        valorFinal =valorCarro * 1.21
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 48:
        valorFinal =valorCarro * 1.24
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 54:
        valorFinal =valorCarro * 1.27
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
    elif  PagamentoParcelado == 60:
        valorFinal =valorCarro * 1.30
        parcelas = valorFinal / PagamentoParcelado
        print(valorFinal)
        print(parcelas)
        