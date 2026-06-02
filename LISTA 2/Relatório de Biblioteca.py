from collections import Counter

arquivo = "livros.txt"

autores = []
maior_qtd = 0
livro_maior = ""

total_livros = 0

with open(arquivo, "r", encoding="utf-8") as f:

    for linha in f:

        titulo, autor, qtd = linha.strip().split(";")

        qtd = int(qtd)

        total_livros += qtd

        autores.append(autor)

        if qtd > maior_qtd:
            maior_qtd = qtd
            livro_maior = titulo

autor_frequente = Counter(autores).most_common(1)[0][0]

print("Total de livros:", total_livros)
print("Autor mais frequente:", autor_frequente)
print("Livro com maior quantidade:", livro_maior)