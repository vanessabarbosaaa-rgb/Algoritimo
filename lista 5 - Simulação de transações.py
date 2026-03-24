try:
    saldo = float(input("Digite o saldo da conta: "))
    valor = float(input("Digite o valor da transferência: "))
    
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    
    saldo -= valor
    print(f"Transferência realizada com sucesso. Saldo restante: {saldo}")

except ValueError as e:
    print(f"Erro: {e}")