Ex- Algoritimo25

numeros = input("Digite números separados por espaço: ").split()

numeros = [float(num) for num in numeros]

numeros.sort()

print("Números em ordem crescente:", numeros)

