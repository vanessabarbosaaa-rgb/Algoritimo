LISTA3
import time

def busca_sequencial(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

n = 100000
lista_ordenada = list(range(1, n + 1))
alvo = 98765

inicio_seq = time.time()
indice_seq = busca_sequencial(lista_ordenada, alvo)
fim_seq = time.time()
tempo_seq = fim_seq - inicio_seq

inicio_bin = time.time()
indice_bin = busca_binaria(lista_ordenada, alvo)
fim_bin = time.time()
tempo_bin = fim_bin - inicio_bin

print("Busca Sequencial: índice =", indice_seq, "tempo =", tempo_seq, "segundos")
print("Busca Binária: índice =", indice_bin, "tempo =", tempo_bin, "segundos")