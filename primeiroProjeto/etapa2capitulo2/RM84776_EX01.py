# Calcular o total de calorias digitadas

# Variavel para armazenar o total de calorias
# Conforme pesquisa, a unidade de medida "caloria" não possui numeros quebrados. Sendo somente inteiros.
total_calorias: int = 0
# Recebe o total de alimentos ingeridos
total_alimentos: int = int(input("Digite o total de alimentos ingeridos: "))
# Executa uma interação no total de alimentos ingeridos
for i in range(1, total_alimentos + 1):
    # Recebe a entrada de calorias para o item atual
    caloria: int = int(input(("Informe as calorias do alimento {}: ".format(i))))
    # Incrementa o total de calorias
    total_calorias += caloria

#Exibe as informações totais.
print("Total de alimentos: {}".format(total_alimentos))
print("Total de calorias: {}".format(total_calorias))