movimentacoes = []

while True:

    tipo = input("D = depósito / S = saque / F = fim: ").upper()

    if tipo == "F":
        break

    valor = float(input("Valor: "))

    movimentacoes.append((tipo, valor))

depositado = sum(v for t, v in movimentacoes if t == "D")
sacado = sum(v for t, v in movimentacoes if t == "S")

print("Total depositado:", depositado)
print("Total sacado:", sacado)