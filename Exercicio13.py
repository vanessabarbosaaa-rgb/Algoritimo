Exercicio13
def maior_menor(lista):
    if not lista:
        return None, None  
    maior = max(lista)
    menor = min(lista)
    return maior, menor

numeros = [3, 7, 1, 9, 4]
maior, menor = maior_menor(numeros)
print("Maior:", maior)
print("Menor:", menor)