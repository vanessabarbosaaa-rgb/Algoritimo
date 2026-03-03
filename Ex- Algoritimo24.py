Ex- Algoritimo24

numeros = input("Digite números separados por espaço: ").split()


numeros = [float(num) for num in numeros]

maior = max(numeros)
menor = min(numeros)

print("O maior número é:", maior)
print("O menor número é:", menor)
