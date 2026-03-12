LISTA3
def busca_aluno(lista):
    
    for nome, nota in lista:
        if nota >= 7 and nome.startswith("A"):
            return nome
    return 

alunos = [
    ("Bruno", 8),
    ("Ana", 9),
    ("Carla", 6),
    ("Alice", 7),
    ("Arthur", 5)
]

resultado = busca_aluno(alunos)
print(resultado) 