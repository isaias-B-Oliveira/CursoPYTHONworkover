print("COVID-19")
suspeitos = 0
num_pac = int(input("Informe a quantidde de pacientes: "))

for x in range(num_pac):
    tosse = int(input("Tosse ? \n 1 = sim \n 2 = nao \n Respo: "))
    febre = int(input("Febre ? \n 1 = sim \n 2 = nao \n Respo: "))
    respi = int(input("Respi ? \n 1 = sim \n 2 = nao \n Respo: "))

    if (tosse == 1 and febre == 1 and respi == 1):
        suspeitos += 1
print("Suspeito de COVID_19: {}".format(suspeitos))        