Ex- Algoritimo22
texto = input("Digite uma frase ou palavra: ").lower()

vogais = "aeiou"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print("O número de vogais é:", contador)
