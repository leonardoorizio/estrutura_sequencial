#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

def salario():

    valor_hr = float(input("Digite quanto você ganha por hora:R$"))
    horas_tb = float(input("Digite quantas horas você trabalha, diáriamente:"))
    salario_mensal = (valor_hr * horas_tb) * 30

    print("Você ganha R${} por hora, trabalha {} horas por dia. Totalizando R${} salário.".format(valor_hr,horas_tb,salario_mensal))

salario()