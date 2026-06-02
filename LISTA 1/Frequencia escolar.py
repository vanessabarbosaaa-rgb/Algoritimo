frequencias = []

total_aulas = int(input("Quantidade de aulas: "))

for i in range(total_aulas):
    presenca = input("P ou F: ").upper()
    frequencias.append(presenca)

presentes = frequencias.count("P")

percentual = (presentes / total_aulas) * 100

print(f"Frequência: {percentual:.2f}%")