alunos = []

def cadastrar():
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso
    }

    alunos.append(aluno)
    print("Aluno cadastrado!")

def listar():
    for aluno in alunos:
        print(aluno)

def buscar():
    matricula = input("Digite a matrícula: ")

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(aluno)
            return

    print("Aluno não encontrado.")

while True:
    print("\n1-Cadastrar")
    print("2-Listar")
    print("3-Buscar")
    print("0-Sair")

    op = input("Opção: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "3":
        buscar()
    elif op == "0":
        break