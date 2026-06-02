arquivo = "livros.txt"

try:

    titulo = input("Título: ")

    if titulo.strip() == "":
        raise ValueError("Título inválido")

    with open(arquivo, "r", encoding="utf-8") as f:

        encontrado = False

        for linha in f:

            if titulo.lower() in linha.lower():
                print(linha)
                encontrado = True

        if not encontrado:
            print("Livro não encontrado")

except FileNotFoundError:
    print("Arquivo inexistente")

except ValueError as erro:
    print(erro)