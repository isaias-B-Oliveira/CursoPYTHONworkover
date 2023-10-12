# crie um programa onde o usuario posa cadastrar um inderteminado numero equipamentos e seus respectivos preços considere que nao tenha precos semelhentes ao fim do cadastro o programa deve informa o produto mais barato e seu preço #

equipamentos = []
precos  = []
while True:
    equi = input("Cadastre o seu equipamento: (ou digite [S] para sair) ")
    if (equi.upper() == "S"):
       break
    if (equi != ""):
       equipamentos.append(equi)
    
    pre = float(input("Agora cadastre o preço do seu equipamento:R$ "))
    if (pre > 0):
        precos.append(pre)

indice_menor_preco =  precos.index(min(precos)) 
indice_preco =  precos.index(min(precos)) 

print("Equipameto mais barato: {}".format(equipamentos[indice_menor_preco])) 
print("Preço do equipamento R$: {}".format(precos[indice_preco])) 

