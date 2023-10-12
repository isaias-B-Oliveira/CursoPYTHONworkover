# Esccreva um programa que reseba duas notas de alunos de programacaaao,
# Em seguida a media ponderada com pesos 2 e 3,
# Deve imprimir a media ponderada obtida

nota1 = float(input("Digite a 1º nota "))
nota2 = float(input("Digite a 2º nota "))
media = (nota1 * 2 + nota2 * 3) / 5

print("Media = {:.1f}".format(media))