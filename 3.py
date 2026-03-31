def ler_quantidade():
    while True:
        try:
            qtd = int(input("Quantidade: "))
            return qtd
        except ValueError:
            print("Erro! Digite apenas números.")

print("Quantidade válida:", ler_quantidade())
 