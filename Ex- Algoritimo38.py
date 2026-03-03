Ex- Algoritimo38
nome_arquivo = "dados.txt"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Esta é a segunda linha.\n")

print("Dados gravados com sucesso!")
