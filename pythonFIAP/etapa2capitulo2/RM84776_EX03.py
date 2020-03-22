# Calcular a senha LIBERDADE somando com o fatorial dos minutos inseridos
# Primeira parte da senha
senha_parte_1: str = "LIBERDADE"
# Segunda parte da senha
senha_parte_2: int = 1
# Valor inteiro não negativo dos minutos (não usar "." ou ",")
minutos:int = int(input("Digite o minuto atual: "))

# Interação nos minutos para buscar o fatorial minutos = minutos * n ....
for i in range(2, minutos + 1):
    senha_parte_2 = senha_parte_2 * i

# Exibe a senha atual com base no resultado do fatorial
print("A SENHA ATUAL É: {}".format(senha_parte_1 + str(senha_parte_2)))