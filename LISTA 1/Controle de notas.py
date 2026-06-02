def calcular_media(notas):
    return sum(notas) / len(notas)

nome = input("Aluno: ")

notas = []

for i in range(3):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")