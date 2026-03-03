Ex- Algoritimo21
palavra = input("Digite uma palavra: ").lower().replace(" ", "")

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
