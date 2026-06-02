arquivo = "livros.txt"

titulo_busca = input("Livro: ")

livros = []

try:
    with open(arquivo, "r", encoding="utf-8") as f:

        for linha in f:
            titulo, autor, qtd = linha.strip().split(";")

            if titulo == titulo_busca:

                qtd = int(qtd)

                if qtd > 0:
                    qtd -= 1
                    print("Empréstimo realizado!")
                else:
                    print("Livro indisponível")

            livros.append(f"{titulo};{autor};{qtd}\n")

    with open(arquivo, "w", encoding="utf-8") as f:
        f.writelines(livros)

except FileNotFoundError:
    print("Arquivo não encontrado")