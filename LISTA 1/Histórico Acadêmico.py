historico = {}

def adicionar_disciplina():
    disciplina = input("Disciplina: ")
    historico[disciplina] = []

def adicionar_nota():
    disciplina = input("Disciplina: ")

    if disciplina in historico:
        nota = float(input("Nota: "))
        historico[disciplina].append(nota)
    else:
        print("Disciplina não encontrada")

def consultar():
    for disciplina, notas in historico.items():
        print(disciplina, notas)

def calcular_cra():
    soma = 0
    quantidade = 0

    for notas in historico.values():
        soma += sum(notas)
        quantidade += len(notas)

    if quantidade > 0:
        print("CRA =", soma / quantidade)

while True:

    print("\n1-Adicionar disciplina")
    print("2-Adicionar nota")
    print("3-Consultar")
    print("4-Calcular CRA")
    print("0-Sair")

    op = input("Escolha: ")

    if op == "1":
        adicionar_disciplina()

    elif op == "2":
        adicionar_nota()

    elif op == "3":
        consultar()

    elif op == "4":
        calcular_cra()

    elif op == "0":
        break