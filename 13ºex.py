#13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

def imc():
    genero = str(input("Qual seu gênero sexual, M para Masculino ou F para Feminino: "))
    altura = float(input("Digite sua altura:"))
    genero = genero.strip().upper()

    if(genero == "M"):
        c1 = (72.7 * altura) - 58
        print("Levando em consideração sua altura {}cm, seu peso ideal seria {}.".format(altura, c1))
    else:
        c2 = (62.1 * altura) - 44.7
        print("Levando em consideração sua altura {}cm, seu peso ideal seria {}.".format(altura, c2))

imc()
