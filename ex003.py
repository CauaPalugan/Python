print("Consultoria de Salários e Descontos! \n")

hrtrab = float(input("Quantas horas você trabalhou: "))
valor = float(input("Qual é o valor recebido por hora: "))
desconto = float(input("Qual é o percentual de desconto(INSS): "))

calculo1 = valor * hrtrab
calculo2 = calculo1 * desconto/100
calculo3 = calculo1 - calculo2

print("\n\nO seu salário bruto é igual á {0:2.2f}".format(calculo1))
print("O valor descontado pelo INSS é igual à {0:2.2f}".format(calculo2))
print("Com os descontos o seu salário líquido é de {0:2.2f}".format(calculo3))