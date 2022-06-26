#4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media_estacio():

    nome_aluno = input("Nome do aluno:")

    n1 = int(input("Digite a nota do 1º semestre:"))
    n2 = int(input("Digite a nota do 2º semestre:"))
    n3 = int(input("Digite a nota do 3º semestre:"))
    n4 = int(input("Digite a nota do 4º semestre:"))

    media_aluno = round((n1+n2+n3+n4) / 4)

    if(media_aluno >= 6):
        print("A média do aluno {}, foi {} APROVADO :)".format(nome_aluno,media_aluno))
    else:
        print("A média do aluno {}, foi {} REPROVADO :(".format(nome_aluno,media_aluno))

media_estacio()



