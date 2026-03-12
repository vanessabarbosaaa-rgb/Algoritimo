Exercicio20
def soma_acumulada(lista):
    acumulada = []
    total = 0
    for num in lista:
        total += num
        acumulada.append(total)
    return acumulada


numeros = [1, 2, 3, 4]
print(soma_acumulada(numeros))