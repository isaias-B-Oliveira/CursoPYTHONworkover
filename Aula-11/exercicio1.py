# crie uma lista com os estados da regiao sudeste
# imprima todos items da lista
# Altere o nomes dos estados para sua capitais
# imprima toda lista usando uma estrutura de repetição

sudeste = ["SaoPaulo", "RiodeJaneiro", "MinasGerais", "EspiritoSanto"]

print(sudeste)

sudeste[0] = "saopauloCapital"
sudeste[1] = "riodejaneiroCapital"
sudeste[2] = "BeloHorizonte"
sudeste[3] = "Vitoria"

for sud in range(4):
    print(sudeste[sud])

