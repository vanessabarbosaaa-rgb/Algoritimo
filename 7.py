alunos = [
    {"matricula": 1001, "nome": "Ana"},
    {"matricula": 1002, "nome": "Bruno"}
]

def buscar_por_matricula(mat):
    try:
        mat = int(mat)
    except ValueError:
        return "Matrícula deve ser número!"

    for aluno in alunos:
        if aluno["matricula"] == mat:
            return aluno["nome"]
    
    return "Aluno não encontrado"

print(buscar_por_matricula("1001"))
print(buscar_por_matricula("abc"))