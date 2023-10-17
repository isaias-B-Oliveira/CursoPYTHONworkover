# inserindo elemento numa matriz manualmente
matriz = [
    [12, 13],
    [23, 20],
    [7, 5],
]

# Outras formas de inserir elemento
l1 = [15, 21]
l2 = [45, 47]
l3 = [4, 8]
M = [l1]
M.append(l2)
M.insert(2, l3)
print(M)

# inserindo dados de uma forma dinamica e aleatoria entre [1 e 10]
import random

while True:
    lin = int(input("Digite quantas linhas tera sua Matriz: "))
    col = int(input("Digite quantas colunas tera sua Matriz: "))
    if(lin > 0 and col > 0):
        Matriz = []

        for i in range(lin):
            Linha = []

            for j in range(col):
                num = random.randint(1, 10)
                Linha.append(num)
            Matriz.append(Linha)
        break   
print(Matriz)

# imprimindo uma matriz formatada
for i in range(lin):
    for j in range(col):
      print(Matriz[i] [j], end = " ")   
    print("")       