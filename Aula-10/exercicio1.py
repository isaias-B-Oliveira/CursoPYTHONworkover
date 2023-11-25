# um programa deve reseber a idade eo sexo dos alunos considere que o usuario
# nao saber a quantidade de alunos, ao fim ele deve exibir a quantidade de rapases
# acima de 18 anos de idade, e a media da idade das moças
# para encerar o programa informe uma idade negativa
rapaz_maio = 0
soma_idade_mocas = 0
mocas = 0
while True:
    sexo  = input("Sexo [M|F]: ")
    idade = int(input("Idade: "))
    if(idade < 0):
      break

    if (sexo.upper() == "M"):
       if (idade > 18):
          rapaz_maio += 1
    elif (sexo.upper() == "F"):
       soma_idade_mocas += idade
       mocas += 1
    else:
       print("Opção de sexo invalida")

media = 0
if (mocas > 0):
    media = soma_idade_mocas / mocas
  
print("Rapazes acima de 18 anos: {}".format(rapaz_maio))
print("Media de idade das moças: {}".format(media))
       
