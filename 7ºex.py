#7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def area_do_quadrado():

    lagura = float(input("Digite a lagura:"))
    comprimento = float(input("Digite o comprimento:"))
    area = (lagura * comprimento) * 2

    print("O dobro da area do quadrado é {} metros quadrados.".format(area))

area_do_quadrado()