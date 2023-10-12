# crie um programa simples onde o usuario possa cadastra produtos depois percorra toda lista usando enumerate e inprima os produtos cadastrado eo seu indice

produtos = []
while True:
    nome = input("Nome: ")
    produtos.append(nome)

    pergunta = input("Deseja continuar [S|N] ")
    if (pergunta.upper() == "N"):
        break


for indice, valor in enumerate(produtos):
    print("{} --> {}".format(indice, valor))
