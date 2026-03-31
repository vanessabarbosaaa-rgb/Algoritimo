vendas = [150, 80, 220, 90, 300]

def busca_binaria_vendas(lista, valor):
    lista_ordenada = sorted(lista)  
    baixo, alto = 0, len(lista_ordenada) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2

        if lista_ordenada[meio] == valor:
            return meio
        elif lista_ordenada[meio] < valor:
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1

print("Índice do valor 220:", busca_binaria_vendas(vendas, 220))