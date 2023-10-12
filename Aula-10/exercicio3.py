# pedir ao usuário para informar 5 números
# Verifica se o número é positivo e par
# Verifica se o número é positivo e impar
# Imprime a quantidade de números pares e impares dos numeros informados

quantidade_pares = 0
quantidade_impares = 0
           
for i in range(5):
    numero = int(input(f"Informe o {i + 1}º número: "))

    if (numero < 0 and numero != int()):
        print("Informe um numero positivo e inteiro")

    if (numero > 0 and numero % 2 == 0):
        quantidade_pares += 1

    if (numero > 0 and numero % 2 != 0):
        quantidade_impares += 1

print(f"Dos 5 números informados, {quantidade_pares} são pares.")
print(f"Dos 5 números informados, {quantidade_impares} são pares.")
