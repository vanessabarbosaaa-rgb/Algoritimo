Ex- Algoritimo37
nome_arquivo = "arquivo.txt"

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print("Número de linhas:", len(linhas))