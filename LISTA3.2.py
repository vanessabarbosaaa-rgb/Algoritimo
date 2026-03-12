LISTA3
def conta_ocorrencias(lista, alvo):
   
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1
    return contador

numeros = [10, 23, 45, 23, 67, 23]
resultado = conta_ocorrencias(numeros, 23)
print(resultado)  