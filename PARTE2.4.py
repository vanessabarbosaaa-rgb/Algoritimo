def busca_insercao(lista, alvo):
  
    esquerda, direita = 0, len(lista)
    while esquerda < direita:
        meio = (esquerda + direita) // 2
        if lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio
    return esquerda