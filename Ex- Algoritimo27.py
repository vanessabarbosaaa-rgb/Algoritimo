Ex- Algoritimo27

numeros = input("Digite números separados por espaço: ").split()

numeros = [float(num) for num in numeros]

soma = sum(numeros)

print("A soma dos elementos da lista é:", soma)
