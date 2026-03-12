LSTA3
def indice_menor(lista):
  
    if not lista:  
        return -1

    menor_valor = lista[0]
    indice_menor = 0

    for i in range(1, len(lista)):
        if lista[i] < menor_valor:
            menor_valor = lista[i]
            indice_menor = i

    return indice_menor

numeros = [10, 23, 5, 45, 2, 67]
resultado = indice_menor(numeros)
print(resultado) 