Ex- Algoritimo26

numeros = input("Digite números separados por espaço: ").split()

numeros = [float(num) for num in numeros]


numeros_sem_duplicatas = []
for num in numeros:
    if num not in numeros_sem_duplicatas:
        numeros_sem_duplicatas.append(num)

print("Lista sem duplicatas:", numeros_sem_duplicatas)