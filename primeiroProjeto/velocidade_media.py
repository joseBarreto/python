#Esse programa recebe a distancia é o tempo e calcula a velocidade média
#primeiro vamos pedir a distância e o tempo

print("Esse é o calculador de velocidade média")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")

#realizando o calculo e exibindo a mensagem
velocidade_media = float(distancia) / float(tempo)
print("A velocidade média calculada foi de {0:.2f} km/h".format(velocidade_media))
