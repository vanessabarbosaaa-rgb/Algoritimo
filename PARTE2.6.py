def valor_mais_proximo(lista, alvo):
    if not lista:
        return -1
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    if esquerda >= len(lista):
        return len(lista) - 1
    if direita < 0:
        return 0
    if abs(lista[esquerda] - alvo) < abs(lista[direita] - alvo):
        return esquerda
    else:
        return direita