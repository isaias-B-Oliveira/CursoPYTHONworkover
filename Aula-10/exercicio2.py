# o usuario informa um valor N
# armazene esse valor en uma variavel N
# o usuario deve digitar N numeros
# deve imprimir a media dos N numeros digitados
# para encerar digite um numero negativo

somaN = 0
Nnumeros = 0
while True:

    Nu = int(input("Digite um número: "))

    if (Nu < 0):
        break
    somaN += Nu
    Nnumeros += 1

media = 0
if (Nnumeros > 0):
    media = somaN / Nnumeros
print("A média dos numeros e: {:.2f}".format(media))
