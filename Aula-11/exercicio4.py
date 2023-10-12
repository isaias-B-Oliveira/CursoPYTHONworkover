# o usuario deve poder digitar N numero inteiros 
# armazene numa lista
# depois pergunte ao usuario ser ele quer apagar os numeros pares ou impares
# de acordo com o que ele escolher apague os numeros 
# depois imprima a nova lista


numeros = []
while True:
    num = int(input("Digite um número (ou digite 0 para parar): "))
    if (num == 0):
        break
    if (num > 0):
        numeros.append(num)

opcao = input("Deseja apagar os números pares ou ímpares da lista? (P/I): ")

if (opcao.upper() == 'P'):
    numeros = [num for num in numeros if num % 2 != 0]
    print("Lista após a remoção dos números pares:", numeros)

elif (opcao.upper() == 'I'):
    numeros = [num for num in numeros if num % 2 == 0]
    print("Lista após a remoção dos números ímpares:", numeros)
else:
    print("Opção inválida. A lista permanece inalterada.")
