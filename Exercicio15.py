Exercicio15
import copy

matriz = [[1, 2], [3, 4]]

matriz_copia = copy.deepcopy(matriz)

matriz_copia[0][0] = 99

print("Original:", matriz)
print("Cópia:", matriz_copia)