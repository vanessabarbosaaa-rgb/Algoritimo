Exercicio3
tarefas = []

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ").strip()
    if nome:
        tarefas.append({"nome": nome, "feito": False})
        print(f'Tarefa "{nome}" adicionada!\n')
    else:
        print("Tarefa vazia não pode ser adicionada.\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.\n")
        return
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "FEITO" if tarefa["feito"] else "ESPERA"
        print(f"{i}. {tarefa['nome']} - {status}")
    print()  

def marcar_concluida():
    if not tarefas:
        print("Nenhuma tarefa para marcar.\n")
        return
    listar_tarefas()
    escolha = input("Digite o número da tarefa que deseja marcar como concluída: ")
    if not escolha.isdigit():
        print("Entrada inválida! Digite um número.\n")
        return
    index = int(escolha) - 1
    if 0 <= index < len(tarefas):
        tarefas[index]["feito"] = True
        print(f'Tarefa "{tarefas[index]["nome"]}" marcada como FEITO!\n')
    else:
        print("Número de tarefa inválido.\n")

def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa para remover.\n")
        return
    listar_tarefas()
    escolha = input("Digite o número da tarefa que deseja remover: ")
    if not escolha.isdigit():
        print("Entrada inválida! Digite um número.\n")
        return
    index = int(escolha) - 1
    if 0 <= index < len(tarefas):
        removida = tarefas.pop(index)
        print(f'Tarefa "{removida["nome"]}" removida!\n')
    else:
        print("Número de tarefa inválido.\n")

while True:
    print("=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")
    print()
    
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        marcar_concluida()
    elif escolha == "4":
        remover_tarefa()
    elif escolha == "5":
        print("Saindo da Lista de Tarefas. Até mais!")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 5.\n")