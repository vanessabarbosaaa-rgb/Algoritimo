def busca_rotated(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        if lista[esquerda] <= lista[meio]:
            if lista[esquerda] <= alvo < lista[meio]:
                direita = meio - 1
            else:
                esquerda = meio + 1
        else:
            if lista[meio] < alvo <= lista[direita]:
                esquerda = meio + 1
            else:
                direita = meio - 1
    return -1