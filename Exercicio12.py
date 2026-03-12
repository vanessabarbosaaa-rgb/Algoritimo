Exercicio12
lista = [1, 2, 2, 3, 4, 4, 5]
nova_lista = []

for num in lista:
    if num not in nova_lista:
        nova_lista.append(num)

print(nova_lista)
