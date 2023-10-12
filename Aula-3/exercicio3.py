# O programa deve ler uma temperatura en farenheith e converter para celcius
# Sabe-se que °C = (°F - 32) / 1.8

fahrenheit = int(input("Digite a temperatura en Fahrenheit: "))
celcius = (fahrenheit - 32) / 1.8

print("Temperatura convertida en Celcius = {:.2f}".format(celcius))