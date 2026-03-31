inventario = {
    "Notebook": {"qtd": 10, "preco": 2500},
    "Mouse": {"qtd": 50, "preco": 80}
}

def consultar_produto(nome):
    dados = inventario.get(nome)
    
    if dados:
        print(f"{nome} - Estoque: {dados['qtd']} | Preço: R${dados['preco']}")
    else:
        print("Produto não encontrado")

consultar_produto("Mouse")
consultar_produto("Headset")