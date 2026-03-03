Ex- Algoritmo40
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

try:
    resultado = numerador / denominador
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")