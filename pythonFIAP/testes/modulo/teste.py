#import calculadora
from calculadora import somar
valor1 = input("Digite o valor: ")
valor2 = input("Digite outro valor: ")
soma = somar(valor1, valor2)

print("A soma é {}".format(soma))
