#10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#(0 °C × 9/5) + 32 = 32 °F

def conversor():
    celcius = float(input("Digite a temperatura em Celsius:"))
    conversao = (celcius * 9/5) + 32

    print("{} Cº representa {} Fº.".format(celcius,conversao))

conversor()
