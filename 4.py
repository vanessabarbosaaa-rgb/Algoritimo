estoque = ["Mouse", "Teclado", "Monitor", "Notebook"]

def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1

print("Índice do Monitor:", busca_sequencial(estoque, "Monitor"))
print("Índice do Celular:", busca_sequencial(estoque, "Celular"))