# crie um programa para cadastra nomes de alunos de uma turma 
# o usuario nao sabe a quantidade de alunos da turma
# armazene numa lista e depais imprima en orden alfabetica

nomes_alunos = []

while True:
    nomes = input("Digite o nome do Aluno(a): ")
    nomes_alunos.append(nomes)

    pergunta = input("Deseja continuar cadastrando [S|N]  ")
    if (pergunta.upper() == "N"):
        break
    
nomes_alunos.sort()
for alunos in nomes_alunos:
    print(alunos)