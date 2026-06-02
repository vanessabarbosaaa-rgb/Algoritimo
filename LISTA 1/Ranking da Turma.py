alunos = {}

qtd = int(input("Quantidade de alunos: "))

for i in range(qtd):
    nome = input("Nome: ")
    media = float(input("Média: "))

    alunos[nome] = media

ranking = sorted(
    alunos.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nRANKING")

for posicao, aluno in enumerate(ranking, start=1):
    print(f"{posicao}º {aluno[0]} - {aluno[1]}")