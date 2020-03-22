# Calcula o bonus com base no tipo de assinatura e faturamento anual

# Solicita o tipo de assinatura e formata o texto para minusculo, para facilitar tratamento posterior
tipo_assinatura: str = input("Digite o tipo da sua assinatura: ").lower()
# Solicita o faturamento anual
faturamento_anual: float = float(input("Digite o faturamento anual: "))

# Calcula qual a porcentagem a ser aplicado no bonus
porcentagem_plano: float = 0

if tipo_assinatura == "basic":
    porcentagem_plano = 0.30
elif tipo_assinatura == "silver":
    porcentagem_plano = 0.20
elif tipo_assinatura == "gold":
    porcentagem_plano = 0.10
elif tipo_assinatura == "platinum":
    porcentagem_plano = 0.05
else:
    print("Plano inválido")
    exit(0)

# Calcula o valor do bonus
bonus: float = faturamento_anual * porcentagem_plano

# Exibe o valor do bonus
print("Valor do Bonus: R${:.2f}".format(bonus))
