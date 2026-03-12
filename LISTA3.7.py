LISTA3
import random

def primeiro_maior_50(lista):
   
    for i, valor in enumerate(lista):
        if valor > 50:
            return (i, valor)
    return (-1, None)  

lista_aleatoria = [random.randint(0, 100) for _ in range(100)]

resultado = primeiro_maior_50(lista_aleatoria)
print("Lista:", lista_aleatoria)
print("Primeiro > 50:", resultado)