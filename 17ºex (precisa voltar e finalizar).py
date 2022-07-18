#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

def calculo_tintas():

    tamanho_metros_quadrados = float(input("Digite o tamanho da area em metros quadrados:"))

    quantidade_de_latas = round(tamanho_metros_quadrados / 6 / 18)
    preco_final_latas = quantidade_de_latas * 80

    quantidade_de_galoes = round(tamanho_metros_quadrados / 6 / 3.6)
    preço_final_galoes = quantidade_de_galoes * 80

    print(f"{tamanho_metros_quadrados} metros quadrados.")
    print(f"{quantidade_de_latas} latas, totalizaria R${preco_final_latas} reais.")
    print(f"{quantidade_de_galoes} galões, totalizaria R${preço_final_galoes} reais.")

calculo_tintas()

