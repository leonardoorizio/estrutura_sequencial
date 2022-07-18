#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def loja_de_tintas():

    largura = float(input("Digite a largura do local a ser pintado:"))
    altura = float(input("Digite a altura do local a ser pintado:"))
    metro_quadrado = largura * altura

    total_em_litros_necessarios = metro_quadrado / 3
    latas_necessarias =(total_em_litros_necessarios / 18)
    custo_final = (latas_necessarias * 80)

    print("Levando em consideração que o local a ser pintado tem {} metros quadrados, será necessario {} latas, totalizando R${}".format(metro_quadrado,latas_necessarias,custo_final))

loja_de_tintas()

