# #1. Construa um programa que simule a venda de um produto. Para isso, o caixa deve
# informar o código, o nome, o preço unitário e a quantidade comprada de N produtos.
# Para resolver esse problema, utilize dicionários. Assim, considere o código do produto como
# sendo a chave do dicionário e os demais dados como sendo os seus respectivos valores, os
# quais devem ser armazenados em uma lista, conforme exemplo abaixo.

# CODIGO (chave)
# 1
# 2
# 3
# 4

# NOME (valor)
# Monitor LED 24"
# Teclado wireless
# Mouse wireless
# Cartucho colorido

# PREÇO UNITARIO (valor)
# 599,99
# 49,26
# 19,90
# 54,00

# COMPREDAS (valor)
# 1
# 1
# 1
# 2

#por fim deve imprimir os items da compra en orden alfabeticas e calcular o subtotal de cada um deles: SUBTOTAL = QUANTIDADE COMPRADA * PREÇO UNITARIO : e apresentar o valor total da compra 

produtos = {}
while True:
    codigo = int(input("Digite o codigo do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quant = int(input("Digite a quantidade de produtos: "))

    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(quant)
    produtos.update({codigo:prod})
     
    resposta = input("Deseja continuar: [N|S] ")
    if resposta == "N" or resposta == "n":
        break

total = 0
for prod in sorted(produtos.values()):
    subtotal = prod[1] * prod[2]
    print(prod[0] + ": R$ {:.2f}".format(subtotal))
    total += subtotal
print(10 * "-")
print("total: R$ {:.2f}".format(total)) 