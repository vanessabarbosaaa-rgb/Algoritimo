Exercicio17
def mesmas_listas(lista1, lista2):
    return sorted(lista1) == sorted(lista2)

a = [1, 2, 3]
b = [3, 1, 2]
c = [1, 2, 2]

print(mesmas_listas(a, b))  
print(mesmas_listas(a, c))  