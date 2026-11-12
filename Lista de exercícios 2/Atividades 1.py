codigoCidade =0 
numeroVeiculos = 0 
numeroAcidentes = 0
maiorAcidente = 0 
menorAcidnte = float('inf')
cidadeMaior = 0 
cidadeMenor = 0
somaTodasCidades = 0

#SC
somaSC = 0
qtdSC = 0 
somaSCAcidentes = 0

#RS
somaRS = 0 
qtdRS = 0
somaRSAcidentes = 0

#PR
somaPR = 0
qtdPR = 0
somaPRAcidentes = 0

for contador in range (1,12):
    codigoCidade = int(input("Digite o código da cidade: "))
    numeroVeiculos = int(input("Digite o númerop de carros: "))
    numeroAcidentes = int(input("Digite o número de acidentes: "))

    if numeroAcidentes > maiorAcidente:
        maiorAcidente = numeroAcidentes 
        cidadeMaior = codigoCidade

    if numeroAcidentes < menorAcidnte:
        menorAcidnte = numeroAcidentes
        cidadeMenor = codigoCidade


    somaTodasCidades += numeroVeiculos

   
    if codigoCidade >= 11 and codigoCidade <= 14:
        somaSC += numeroVeiculos
        somaSCAcidentes += numeroAcidentes
        qtdSC += 1 


    if codigoCidade >= 21 and codigoCidade <= 24:
        somaRS += numeroVeiculos
        somaRSAcidentes += numeroAcidentes
        qtdRS += 1 

    if codigoCidade>= 31 and codigoCidade <=34:
        somaPR += numeroVeiculos
        somaPRAcidentes += numeroAcidentes
        qtdPR += 1 


print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
print("A média de veículos em SC: ", (somaSC / qtdSC))
print("A média de acidentes em SC: ", (somaSCAcidentes / qtdSC))
print("A média de veículos em RS: ", (somaRS / qtdRS))
print("A média de acidentes em RS: ", (somaRSAcidentes / qtdRS))
print("A média de veículos em PR: ", (somaPR / qtdPR))
print("A média de acidentes em PR: ", (somaPRAcidentes / qtdPR))