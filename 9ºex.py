#9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
#(32 °F − 32) × 5/9 = 0 °C

def conversor_de_temperatura():

    fahrenheit = float(input("enter the temperature:"))
    celcius = round((fahrenheit - 32) * 5/9)

    print("{}ºF é o equivalente a {}ºC".format(fahrenheit,celcius))

conversor_de_temperatura()

