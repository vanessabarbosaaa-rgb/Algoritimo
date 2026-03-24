try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"Resultado: {resultado}")

except ValueError:
    print("Erro: Você deve digitar números válidos.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

    