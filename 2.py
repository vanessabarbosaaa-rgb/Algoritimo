
alunos = {"João": 8.5, "Maria": 9.0}

def atualizar_nota(nome, nota):
    if nome in alunos:
        print(f"Nota de {nome} atualizada de {alunos[nome]} para {nota}")
    else:
        print(f"Aluno {nome} adicionado com nota {nota}")
    
    alunos[nome] = nota

atualizar_nota("Pedro", 7.5)
print(alunos)
