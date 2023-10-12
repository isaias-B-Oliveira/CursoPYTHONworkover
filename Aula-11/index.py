# Lista vazia
notas = []

# Lista com elementos
notas = [2, 5, 6, 10, 5]

# imprimindo um elemento especifico
print(notas[2])

#mudando um elemento 
notas[4] = 7

# inprimindo todos elementos
for bim in range(5):
    print(notas[bim])

# Adcionando elementos ao final da lista
alunos = ["jose", "pedro", "antonio"]
alunos.append("joao")
alunos.append("jose")
print(alunos)
# escolhendo a posiçao onde sera inserido  
alunos.insert(1, "guilherme")
print(alunos)    

# ordenando a lista alfabeticamente
alunos.sort()
print(alunos)

# ordenando decrecentemente / reverte a orden da lista
alunos.sort(reverse = True)
print(alunos)

# enbaralhando os elementos da lista
import random
random.shuffle(alunos)
print(alunos)

# contando a quantidade dos elementos da lista 
print(len(alunos))
# vendo quantas vezes o elemento se repete na lista
print(alunos.count("jose")) 


idade = [10, 12, 20, 35, 45, 5, 18, 25, 32]
idade.append(35)
idade.append(35)

# acesando o menor elemento
print("Menor idade: {}".format(min(idade)))
# acesando o maior elemento
print("Maior idade: {}".format(max(idade)))
# somando os elementos
print("Soma das idades: {}".format(sum(idade)))
# obtendo a media dos elementos
media = sum(idade) / len(idade)
print("Media das idades: {:.2f}".format(media))
# removendo o ultimo elemento da lista 
idade.pop()
# removendo um elemento especifico
idade.pop(1)
# apagando toda a lista
# idade.clear()
# apagando um item especifico da lista passando o parametro
idade.remove(35)  # so apaga a primeira ocorencia
# percorrendo uma lista e apagando todas as ocorrencias do parametro
for ano in idade:
    if (ano == 35):
        idade.remove(ano)
print(idade)
# verificando se o elemento tem na lista
if (35 in idade):
    print("esse elemento esta na lista")


corredor = ["joao", "jose", "pedro", "guto", "bruno"]
tempo    = [2.30, 2.48, 2.45, 3.00, 2.29]

# como localizar o indice de um elemento na lista
indice_melhor_tempo = tempo.index(min(tempo))
indice_pior_tempo = tempo.index(max(tempo))

print("o corredor com o melhor tempo e {}".format(corredor[indice_melhor_tempo]))    
print("o corredor com o pior tempo e {}".format(corredor[indice_pior_tempo]))    

