# Construa uma função chamada gera_matriz_aleatoria() que tem como
# argumentos o número de linhas e o número de colunas de uma matriz. Como resposta,
# a função deve retornar a matriz gerada cujos valores variam no intervalo [1, 10]. Ao fim
# o programa chamador deve imprimir a matriz.

from funcoens_exercicios import *

lin = int(input("Informe a quantidade de linhas da Matriz: "))
col = int(input("Informe a quantidade de colunas da Matriz: "))

if (lin >= 2 and col >= 2):
    M = gera_matriz_aleatoria(lin, col)
    imprimi_matriz(M)
else:
    print("os valores informados presisao ser maior que [2]: ")   