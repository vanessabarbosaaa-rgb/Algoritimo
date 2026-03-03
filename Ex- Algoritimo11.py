Ex- Algoritimo11
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade grau 1")
elif imc < 40:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3")
