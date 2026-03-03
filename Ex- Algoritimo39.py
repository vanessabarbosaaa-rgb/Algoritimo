Ex- Algoritimo39
opcao = 0

while opcao != 4:
    print("\n=== MENU ===")
    print("1 - Dizer Olá")
    print("2 - Mostrar Soma de dois números")
    print("3 - Mostrar uma mensagem especial")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá! 😄")
    elif opcao == 2:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Soma:", a + b)
    elif opcao == 3:
        print("Você escolheu a mensagem especial!")
    elif opcao == 4:
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")
