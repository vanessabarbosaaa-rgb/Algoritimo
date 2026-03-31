estoque = [
    {"nome": "Notebook Dell", "quantidade": 8, "preco": 2899.90},
    {"nome": "Mouse Logitech", "quantidade": 45, "preco": 89.90},
    {"nome": "Teclado Mecânico", "quantidade": 12, "preco": 249.90},
    {"nome": "Monitor 24''", "quantidade": 15, "preco": 899.90}
]

def cadastrar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except ValueError:
        print("Erro: quantidade e preço devem ser números!")
        return
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print(f"Produto {nome} cadastrado com sucesso!")

def buscar_produto(nome_busca):
    for produto in estoque:
        if produto["nome"].lower() == nome_busca.lower():
            return produto
    return None

def atualizar_quantidade(nome, quantidade_alterada):
    produto = buscar_produto(nome)
    if produto:
        produto["quantidade"] += quantidade_alterada
        print(f"Estoque atualizado! {nome} agora tem {produto['quantidade']} unidades.")
    else:
        print("Produto não encontrado!")

def produto_mais_barato_acima_de(preco_minimo):
    # Ordena estoque pelo preço
    estoque_ordenado = sorted(estoque, key=lambda x: x["preco"])
    baixo = 0
    alto = len(estoque_ordenado) - 1
    resultado = None

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if estoque_ordenado[meio]["preco"] >= preco_minimo:
            resultado = estoque_ordenado[meio]
            alto = meio - 1
        else:
            baixo = meio + 1

    if resultado is None:
        return "Nenhum produto encontrado acima desse preço."
    return f"Produto mais barato acima de R${preco_minimo:.2f}: {resultado['nome']} - R${resultado['preco']:.2f}"

def gerar_relatorio():
    if not estoque:
        print("Estoque vazio!")
        return
    total_estoque = 0
    print("\n--- Relatório de Estoque ---")
    for produto in estoque:
        valor_total = produto["quantidade"] * produto["preco"]
        total_estoque += valor_total
        print(f"{produto['nome']:25} | Qtd: {produto['quantidade']:3} | Preço: R${produto['preco']:.2f} | Total: R${valor_total:.2f}")
    print(f"\nValor total em estoque: R${total_estoque:.2f}")

def menu():
    while True:
        print("\n=== TechZone - Controle de Estoque ===")
        print("1. Cadastrar novo produto")
        print("2. Buscar produto")
        print("3. Atualizar quantidade")
        print("4. Produto mais barato acima de um preço")
        print("5. Gerar relatório completo")
        print("6. Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            nome = input("Digite o nome do produto: ")
            prod = buscar_produto(nome)
            if prod:
                print(f"Encontrado: {prod['nome']} - Qtd: {prod['quantidade']} - R${prod['preco']:.2f}")
            else:
                print("Produto não encontrado.")
        elif opcao == 3:
            nome = input("Nome do produto: ")
            try:
                qtd = int(input("Quantidade a adicionar/subtrair (use negativo para saída): "))
                atualizar_quantidade(nome, qtd)
            except ValueError:
                print("Quantidade inválida!")
        elif opcao == 4:
            try:
                preco = float(input("Preço mínimo: R$"))
                print(produto_mais_barato_acima_de(preco))
            except ValueError:
                print("Preço inválido!")
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
