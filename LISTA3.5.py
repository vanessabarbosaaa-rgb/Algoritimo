LISTA3
def primeiro_adulto(alunos):
   
    for aluno in alunos:
        if aluno["idade"] >= 18:
            return aluno["nome"]
    return None  

lista_alunos = [
    {"nome": "Ana", "idade": 17},
    {"nome": "João", "idade": 25},
    {"nome": "Carla", "idade": 16}
]

resultado = primeiro_adulto(lista_alunos)
print(resultado)  