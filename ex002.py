print("Calculador de Consumo KMs por Litros \n")

distancia = float(input("Qual a distância percorrida na viagem:  \n"))
consumo = float(input("Quantos litros de combustível foi gasto na viagem: \n"))

calculo = distancia/consumo

print("Com base nas informações inseridas acima, seu carro faz {0:2.2f}KMs por Litro!".format(calculo))