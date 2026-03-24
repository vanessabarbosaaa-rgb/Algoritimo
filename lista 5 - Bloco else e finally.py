try:
    numero = int(input("Digite um número: "))
    
    if numero > 10:
        print("Número válido.")

except ValueError:
    print("Erro: Digite um número inteiro válido.")

else:
    print("Programa executado com sucesso.")

finally:
    print("Programa encerrado.")