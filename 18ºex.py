#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def teste_de_velocidade():

    tamanho_do_arquivo = float(input("Digite o tamanho do arquivo:"))
    velocidade_download = float(input("Digite a velocidade de download em Mbps:"))
    calculo = tamanho_do_arquivo / (velocidade_download / 8)

    print(f"Sua internet levará {calculo} segundos para completar o download.")

teste_de_velocidade()
