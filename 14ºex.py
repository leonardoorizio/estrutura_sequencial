#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
# variável multa o valor da multa que João deverá pagar.Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso do Peixe:"))
permitido = 50.0
excesso = peso - permitido
multa = excesso * 4.0

def programa_do_pescador():

    if peso > permitido:
        print("De acordo com regulamento de pesca do estado de São Paulo, você exceu {}kg do permitido. Terá que pagar R${} de multa".format(excesso,multa))
    else:
        print("Parabéns, seu Peixe esta dentro do peso permitido.")

programa_do_pescador()


