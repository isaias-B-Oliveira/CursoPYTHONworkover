
# funcao do exercicio-1
def calcula_distancia_ponto(xA, yA, xB, yB):
    from math import sqrt
    return sqrt((xB - xA) ** 2 + (yB - yA) ** 2) 

# funcao do exercicio-2
def calcula_area_losango(D1, D2):
    return (D1 * D2) / 2

# funcao do exercicio-3
def gera_matriz_aleatoria(lin, col):
    import random
    while True:
        M = []
        for i in range(lin):
            linha = []
            for j in range(col):
                num = random.randint(1, 10)
                linha.append(num)
            M.append(linha)
        break
    return M  
# funcao do exercicio-3
def imprimi_matriz(M):
    lin = len(M)
    col = len(M[0])
    for i in range(lin):
        for j in range(col):
            print(M [i] [j], end = " ")   
        print("")  
    return    
 
            