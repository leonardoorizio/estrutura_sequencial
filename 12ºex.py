#12.Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def imc_cliente():
    altura = float(input("Digite sua altura:"))
    peso_ideal = (72.7 * altura) - 58

    print("Levando em consideração sua altura, que é {}cm. Seu peso ideal seria {}.".format(altura,peso_ideal))

imc_cliente()