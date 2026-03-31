estoque = ["Notebook", "Mouse", "Teclado"]

def adicionar_produto(lista, produto):
    if produto not in lista:
        lista.append(produto)
    print("Estoque atual:", lista)

adicionar_produto(estoque, "Monitor")
adicionar_produto(estoque, "Mouse")
