# Calcular a media de uma turma separando entre Ímpar e Par
total_alunos: int = 50
total_nota_impar: float = 0
total_nota_par: float = 0

for i in range(1, total_alunos + 1 , 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    nota_aluno: float = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    total_nota_impar += nota_aluno

for i in range(2, total_alunos + 1, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_aluno: float = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    total_nota_par += nota_aluno

media_notas_impares: float = total_nota_impar / (total_alunos / 2)
media_notas_pares: float = total_nota_par / (total_alunos / 2)

print("MEDIA DOS ALUNOS ÍMPARES: {}".format(media_notas_impares))
print("MEDIA DOS ALUNOS PARES: {}".format(media_notas_pares))

if media_notas_impares > media_notas_pares:
    print("GRUPO COM MAIOR NOTA: ÍMPA")
elif media_notas_pares > media_notas_impares:
    print("GRUPO COM MAIOR NOTA: PAR")
else:
    print("GRUPO COM MAIOR NOTA: EMPATE (AMTES TEM A MESMA NOTA MEDIA)")

