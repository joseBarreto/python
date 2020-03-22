#Calcular o IMC atravez das entradas de dados: Peso e Altura

#Solicita o peso
peso: float = float(input("Digite seu peso: "))
#Solicita a altura
altura: float = float(input("Digite sua altura: "))
#Calcula o IMG = peso / altura²
imc: float = peso / (altura * 2)

#Procura pela faixa do IMC calculado
faixa_imc: str = ""

if imc < 16.00:
    faixa_imc = "Baixo peso Grau III"
elif imc >= 16.00 and imc <= 16.99:
    faixa_imc = "Baixo peso Grau II"
elif imc >= 17.00 and imc <= 18.49:
    faixa_imc = "Baixo peso Grau I"
elif imc >= 18.5 and imc <= 24.99:
    faixa_imc = "Peso ideal"
elif imc >= 25 and imc <= 29.99:
    faixa_imc = "Sobrepeso"
elif imc >= 30 and imc <= 34.99:
    faixa_imc = "Obesidade Grau I"
elif imc >= 35 and imc <= 39.99:
    faixa_imc = "Obesidade Grau II"
elif imc >= 40:
    faixa_imc = "Obesidade Grau III"

#Apresenta as informações de IMC
print("IMC Calculado: {:.2f}".format(imc))
print("Faixa do IMC: {}".format(faixa_imc))

