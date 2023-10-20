from funcoens import *

saldar()

saldar_aluno("isaias")

print(calcular_dobro(5))  

print(calcular_dobro_triplo(5))

print(10*"-")

print(calcular_area_circulo())

print(10*"-")

lista = [7, 2, 3, 4]
menor, maior, media = retorna_meno_maio_media(lista)
print("menor elemento: {}".format(menor))
print("maior elemento: {}".format(maior))
print("media elementos: {}".format(media))

print(10*"-")

varX = 7
varY = 3
dobroX, triploY = calcular_dobroX_triploY(varX, varY)   
print("dobro de {} = {}".format(varX, dobroX))
print("triplo de {} = {}".format(varY, triploY))

print(10*"-")

print(calcular_IMC(85, 1.69, "Isias"))