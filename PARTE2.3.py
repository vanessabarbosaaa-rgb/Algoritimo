def ultima_ocorrencia(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    resultado = -1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            resultado = meio
            esquerda = meio + 1 
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return resultado