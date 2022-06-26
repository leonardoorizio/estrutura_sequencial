#11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

def calculadora():
    n1 = int(input("Digite um numero inteiro:"))
    n2 = int(input("Digite um numero inteiro:"))
    n3 = float(input("Digite um numero com casas decimais:"))

    a = (n1 * 2) + (n2 / 2)
    b = (n1 * 3) + n3
    c = n3 ** 2

    print("O produto do dobro do primeiro com metade do segundo é {}.".format(a))
    print("A soma do triplo do primeiro com o terceiro é {}.".format(b))
    print("O terceiro elevado ao cubo é {}.".format(c))

calculadora()