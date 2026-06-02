movimentacoes = [
    "Depósito R$ 500",
    "Saque R$ 100",
    "Depósito R$ 200"
]

with open("movimentacoes.txt", "w", encoding="utf-8") as arquivo:

    for item in movimentacoes:
        arquivo.write(item + "\n")

print("Movimentações salvas")