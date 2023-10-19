# imprimindo um elemento do dicionario
contato = {"contato1@gmail.com":"Isaias",
           "contato2@gmail.com":"Isaias2"}

print(contato["contato1@gmail.com"])
#asesando um elemento usando get
print(contato.get("contato2@gmail.com"))
#atualizando e inserindo um elemento usando update
contato.update({"contato1@gmail.com":"Isaias1"})
contato.update({"contato3@gmail.com":"Isaias3"})
print(contato)

# Como localizar um elemento num dicionario
email = input("Digite um Email: ")
if (email in contato):
    print("Esse email e de: {}".format(contato.get(email)))
else:
    print("Nao consta esse email no dicionario: ")

# imprimindo todos os elementos
print("quantidade de elementos: {}".format(len(contato)))

# imprimindo as chaves do dicionario usando keys
for Email in contato.keys():
    print(Email)

# imprimindo os valores do dicionario usando values
for nomes in contato.values():
    print(nomes)

# imprimindo as chaves e os valores usando items
for Email, nomes in contato.items():
    print("O email {} e de {}".format(Email, nomes))  

# ordenando os elementos(chaves) de um dicionario usando sorted 
for Email, nomes in sorted(contato.items()):
    print("{}-->{}".format(Email, nomes))   

# ordenando os elementos(valores cresente) de um dicionario usando itemgetter
alunos = {"jose":1.78,
          "isaias":1.69,
          "oliveira":1.82,
          "junior":1.77}
from operator import itemgetter
for nome, altura in sorted(alunos.items(),key=itemgetter(1)):
    print("{}--> {:.2f}m".format(nome, altura)) 

# ordenando os elementos(valores decresente) de um dicionario usando itemgetter
for nome, altura in sorted(alunos.items(), key=itemgetter(1), reverse=True):
    print("{}--> {:.2f}m".format(nome, altura))

# removendo um item aparti de uma chave especifica usando pop
alunos.pop("junior")
print(alunos)
# removendo o ultimo item do dicionario usando popitem
alunos.popitem()
print(alunos)
# apagando todo dicionario usando clear
alunos.clear()
print("todo dicionario apagado:", alunos)


