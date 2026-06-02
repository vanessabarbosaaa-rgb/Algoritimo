arquivo = "livros.txt"

titulo = input("Título: ")
autor = input("Autor: ")
quantidade = input("Quantidade: ")

with open(arquivo, "a", encoding="utf-8") as f:
    f.write(f"{titulo};{autor};{quantidade}\n")

print("Livro cadastrado!")