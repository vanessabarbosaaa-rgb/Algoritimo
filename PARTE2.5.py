def busca_string_binaria(lista, alvo):
    alvo_lower = alvo.lower()
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio].lower() == alvo_lower:
            return meio
        elif lista[meio].lower() < alvo_lower:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1