# Construa um programa que solicite ao usuário os dados necessários para cálculo da
# área de um losango. Em seguida, com base nos argumentos informados, crie uma
# função chamada calcula_area_losango () para retornar a área da figura. Por fim, o
# programa deve imprimir a área calculada.

from funcoens_exercicios import *

D1 = float(input("Dgite a maior diagonal do losango: "))
D2 = float(input("Dgite a menor diagonal do losango: "))

area = calcula_area_losango(D1, D2)
print("A area do losango e: {}".format(area))