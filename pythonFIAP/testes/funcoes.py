def calcularVelocidadeMedia(distancia, tempo):
    # calcular a velocidade média
    velocidade_media = distancia / tempo
    # retornar o resultado
    return velocidade_media


# solicitar a distancia
distancia = float(input("Digite a disância percorrida: "))
tempo = float(input("Digite o tempo da viagem: "))

# exibir o resultado
print("A velocidade média é {} km/h".format(calcularVelocidadeMedia(distancia, tempo)))
