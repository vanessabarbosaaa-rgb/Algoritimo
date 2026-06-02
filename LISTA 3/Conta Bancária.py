saldo = 0
extrato = []

def deposito(valor):
    global saldo
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")

def saque(valor):
    global saldo

    if valor <= saldo:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
    else:
        print("Saldo insuficiente")

def consultar_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")

def mostrar_extrato():
    print("\nEXTRATO")
    for item in extrato:
        print(item)

while True:

    print("\n1-Depositar")
    print("2-Sacar")
    print("3-Saldo")
    print("4-Extrato")
    print("0-Sair")

    op = input("Opção: ")

    if op == "1":
        valor = float(input("Valor: "))
        deposito(valor)

    elif op == "2":
        valor = float(input("Valor: "))
        saque(valor)

    elif op == "3":
        consultar_saldo()

    elif op == "4":
        mostrar_extrato()

    elif op == "0":
        break