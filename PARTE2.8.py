def busca_matriz_ordenada(matriz, alvo):

    if not matriz:
        return -1, -1
    linhas, colunas = len(matriz), len(matriz[0])
    i, j = 0, colunas - 1
    while i < linhas and j >= 0:
        if matriz[i][j] == alvo:
            return i, j
        elif matriz[i][j] > alvo:
            j -= 1
        else:
            i += 1
    return -1, -1