#6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def raio_circulo():

    diametro = float(input("Digite o diâmetro do circulo:"))
    raio = diametro / 2

    print("A area do circulo é de {}cm".format(raio))

raio_circulo()