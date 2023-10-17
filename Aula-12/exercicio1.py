# o usuario deve informa a horden de uma matriz quadrada. o programa deve gerar valores aleatorios na orden entre 1 e 10: deve calcular a media aritimetica do maior elemento da diagonal prncipal eo menor elemento da diagonal secundaria 
# considere diagonal principal = i == j 
# diagonal secundaria  = i + j == orden + 1


import random

orden = int(input("Informe a orden da matriz: "))
if(orden >= 2):
    while True:
        M = []
        for i in range(orden):
            linha = []
            for j in range(orden):
                num = random.randint(1, 10)
                linha.append(num)
            M.append(linha)
        break

    DiagonalPrincipal = []
    DiagonalSecundaria = []
    for i in range(orden):
        for j in range(orden):
            print(M [i] [j], end = " ")
            if(i == j):
                DiagonalPrincipal.append(M[i] [j])
            elif(i + j == (orden - 1)):
                DiagonalSecundaria.append(M[i] [j])    
        print("")

    maior_DP = max(DiagonalPrincipal)
    menor_DS = min(DiagonalSecundaria)
    media = (maior_DP + menor_DS) / 2
    print("Media = {:.2f}".format(media))

else:
    print("informe uma orden valida: (Maior que 2)")
       
