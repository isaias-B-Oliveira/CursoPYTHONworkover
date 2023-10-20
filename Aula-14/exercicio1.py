# Construa um programa no qual o usuário informe as coordenadas de 2 pontos no
# espaço R2. Em seguida, construa a função calcula_distancia_pontos () para
# retornar a distância entre os pontos, cujos argumentos são as suas respectivas
# coordenadas X e Y. O programa que invocou a função deve exibir a distância entre os
# dois pontos.

from funcoens_exercicios import *

xA = float(input("Digite o valor da cordenada X do ponto A: "))
yA = float(input("Digite o valor da cordenada Y do ponto A: "))
xB = float(input("Digite o valor da cordenada X do ponto B: "))
yB = float(input("Digite o valor da cordenada Y do ponto B: "))

distancia_AB = calcula_distancia_ponto(xA, yA, xB, yB)
print("A distancia dos pontos A e B e: {:.2f}".format(distancia_AB))
