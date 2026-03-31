catalogo = [101, 205, 310, 450, 520]
precos = [50.0, 120.0, 80.0, 200.0, 150.0]

def busca_binaria(codigos, precos, codigo):
    baixo = 0
    alto = len(codigos) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2

        if codigos[meio] == codigo:
            return precos[meio]
        elif codigos[meio] < codigo:
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1 

print("Preço do código 310:", busca_binaria(catalogo, precos, 310))