saldo = 1000

try:

    valor = float(input("Valor do saque: "))

    if valor <= 0:
        raise ValueError("Valor inválido")

    if valor > saldo:
        raise Exception("Saldo insuficiente")

    saldo -= valor

    print("Saque realizado!")

except ValueError:
    print("Digite apenas números válidos")

except Exception as erro:
    print(erro)