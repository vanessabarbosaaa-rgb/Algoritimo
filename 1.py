import os

alunos = []

def adicionar_aluno():
    """Solicita o nome e notas do aluno, calcula a média e adiciona à lista."""
    nome = input("Nome do aluno: ").strip()
    
    notas = []
    while True:
        try:
            num_notas = int(input("Quantas notas deseja informar (2 a 5)? "))
            if 2 <= num_notas <= 5:
                break
            else:
                print("Informe um número entre 2 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    
    media = round(sum(notas) / len(notas), 2)
    aluno = {"nome": nome, "notas": notas, "media": media}
    alunos.append(aluno)
    print(f"{nome} adicionado com média {media}.\n")

def ordenar_alunos():
    """Ordena a lista de alunos pela média em ordem decrescente."""
    alunos.sort(key=lambda x: x["media"], reverse=True)

def salvar_em_arquivo():
    """Salva os dados dos alunos em um arquivo, tratando possíveis erros."""
    arquivo = "alunos.txt"
    
    if os.path.exists(arquivo):
        escolha = input("O arquivo já existe. Deseja sobrescrever? (s/n): ").strip().lower()
        if escolha != "s":
            print("Operação cancelada. Os dados não foram salvos.")
            return
    
    try:
        with open(arquivo, "w") as f:
            for aluno in alunos:
                f.write(f"{aluno['nome']},{aluno['media']}\n")
        print(f"Os dados foram salvos no arquivo '{arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

def exibir_alunos():
    """Exibe os alunos ordenados pela média."""
    print("\nAlunos ordenados por média:")
    for aluno in alunos:
        print(f"{aluno['nome']} - Média: {aluno['media']}")

def main():
    while True:
        adicionar_aluno()
        continuar = input("Deseja adicionar outro aluno? (s/n): ").strip().lower()
        if continuar != "s":
            break

    ordenar_alunos()
    exibir_alunos()
    salvar_em_arquivo()

if __name__ == "__main__":
    main()