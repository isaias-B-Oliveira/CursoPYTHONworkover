# o programa deve receber sexo, peso e altura e mostrar o peso ideal para cada pessoa
# baseado nas informaçoens abaixo
# homens  : (72.7 * altura) - 58.0
# mulheres : (62.1 * altura) - 44.7

sexo = input("Digite seu sexo [M | F]: ")
altura = float(input("Digite sua estatura: "))

if (sexo.upper() == "M"):
    peso = (72.7 * altura) - 58
    print("Seu peso ideal e {:.2f} KG:".format(peso))
elif (sexo.upper() == "F"):
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal e {:.2f} KG".format(peso))
else:
    print("Opção de sexo nao informada")