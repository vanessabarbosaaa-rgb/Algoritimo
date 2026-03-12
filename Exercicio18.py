Exercicio18
import random

numeros = [random.randint(1, 50) for _ in range(10)]
print("Lista original:", numeros)

pares_ordenados = sorted([x for x in numeros if x % 2 == 0])

indice_par = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = pares_ordenados[indice_par]
        indice_par += 1

print("Lista com pares ordenados:", numeros)