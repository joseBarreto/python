valor_compra: float = float(input("Digite o valor da compra: "))
forma_pagamento: int = int(input("1 - Dinheiro / 2 - Cartão: "))

if valor_compra > 100 or forma_pagamento == 1:
    valor_compra = valor_compra * 0.9
    print("Você tem direito á um desconto!")

print("O valor a pagar é {}".format(valor_compra))
