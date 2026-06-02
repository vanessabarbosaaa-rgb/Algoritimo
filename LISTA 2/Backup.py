def backup(origem, destino):

    with open(origem, "r", encoding="utf-8") as arquivo_origem:

        conteudo = arquivo_origem.read()

    with open(destino, "w", encoding="utf-8") as arquivo_destino:

        arquivo_destino.write(conteudo)

    print("Backup realizado!")

backup("livros.txt", "backup_livros.txt")