def saldar():
    print("Ola!")

def saldar_aluno(nome):
    print("Ola {}".format(nome))

# como documenta uma funcao
def calcular_dobro(numero):
    "esta funcao recebe um numero parametro e devolve o seu dobro"
    return 2 * numero

def calcular_dobro_triplo(numero):
    return 2 * numero, 3 * numero


valor_PI = 3.14
def calcular_area_circulo():
    raio = 3
    return valor_PI * pow(raio, 2)

def retorna_meno_maio_media(lista):
    menor = min(lista)
    maior = max(lista)
    media = sum(lista) / len(lista)
    return menor, maior, media

def calcular_dobroX_triploY(X, Y):
    return 2 * X, 3 * Y

#definindo um parametro default, se nao informado o nome tera prezado como padrao, esses parametros presizao ser os ultimos
def calcular_IMC(peso, altura, nome = "prezado(a)"):
    imc = peso / pow(altura, 2)
    return "{}, seu imc e {:.2f}.".format(nome, imc)

