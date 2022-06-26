#5.Faça um Programa que converta metros para centímetros.

def apresentacao():
    print("***************************")
    print("Welcome to magic calculator")
    print("***************************")

def calculadora():

    metros = round(float(input("Digite em metros o tamanho que deseja converter:")))
    centimetros = round(metros * 100)
    print("{} metros é igual a {} centímetros.".format(metros,centimetros))

apresentacao()
calculadora()

