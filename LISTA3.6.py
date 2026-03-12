LISTA3
def busca_matriz(matriz, alvo):
   
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == alvo:
                return (i, j)  
    return (-1, -1)  

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = busca_matriz(matriz, 5)
print(resultado)  