Ex- Algoritimo12
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1  # assume que o primeiro número é o maior

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print("O maior número é:", maior)
