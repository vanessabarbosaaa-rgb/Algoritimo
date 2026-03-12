LISTA3
def busca_sequencial(lista, alvo):
   
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  
    return -1  

numeros = [10, 23, 45, 23, 67]
resultado = busca_sequencial(numeros, 23)
print(resultado)  