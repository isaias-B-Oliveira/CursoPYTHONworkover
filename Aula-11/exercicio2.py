# fasa um programa onde o usuario posa digitar quantos times ele quiser
# armazene numa lista 
# depois imprima usando uma laço de repetiçao

times = []

while True:
    nome = input("Digite os nomes dos times: ")
    times.append(nome)

    resp = input("Deseja continia [S|N] ")
    if (resp.upper() == "N"):
        break

for TIMES in times:
    print(TIMES)    
