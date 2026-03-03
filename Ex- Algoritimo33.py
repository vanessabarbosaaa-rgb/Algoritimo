Ex- Algoritimo33
import math

def area_circulo(raio):
    return math.pi * (raio ** 2)

raio = float(input("Digite o raio do círculo: "))
area = area_circulo(raio)

print("Área do círculo:", area)