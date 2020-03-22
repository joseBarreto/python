# Calcula o maior dia com base na votação

# Solicita a quantidade de votos de cada dia da semana
segunda: int = int(input("Digite a quantidade de votos da segunda-feira: "))
terca: int = int(input("Digite a quantidade de votos da terça-feira: "))
quarta: int = int(input("Digite a quantidade de votos da quarta-feira: "))
quinta: int = int(input("Digite a quantidade de votos da quinta-feira: "))
sexta: int = int(input("Digite a quantidade de votos da sexta-feira: "))

# Verifica qual o dia vencedor
# Neste caso, poderiamos usar o import da Math e usar a função Max, porém como exercicio didatico vamos usar condições de ifs
# Também estamos levando em conta que o primeiro dia (a contar de segunda -> sexta) com mais voto vence, não tendo empates
dia_vencedor: str = ""
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    dia_vencedor = "segunda-feira"
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    dia_vencedor = "terça-feira"
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    dia_vencedor = "quarta-feira"
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    dia_vencedor = "quinta-feira"
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    dia_vencedor = "sexta-feira"
else:
    print("possível empate")
    exit(0)

print("O dia vencedor, para exibição das lives, é: {}".format(dia_vencedor))
