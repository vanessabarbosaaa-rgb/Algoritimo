import os
import csv

livros = []

def adicionar_livro():

    titulo = input("Título do livro: ").strip()
    if not titulo:
        print("Erro: O título não pode estar vazio.")
        return

    autor = input("Autor: ").strip()
    if not autor:
        print("Erro: O autor não pode estar vazio.")
        return


    for livro in livros:
        if livro['titulo'].lower() == titulo.lower() and livro['autor'].lower() == autor.lower():
            print(f"Aviso: O livro '{titulo}' de {autor} já está cadastrado.")
            return

    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano <= 0:
                raise ValueError("O ano deve ser positivo.")
            if ano > 2100:
                print("Ano muito alto. Verifique se está correto.")
                continue
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

    while True:
        try:
            paginas = int(input("Número de páginas: "))
            if paginas <= 0:
                raise ValueError("O número de páginas deve ser positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

    livro = {"titulo": titulo, "autor": autor, "ano": ano, "paginas": paginas}
    livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livros():

    if not livros:
        print("Nenhum livro cadastrado.")
        return
    print("\n" + "="*60)
    print("LISTA DE LIVROS")
    print("="*60)
    for i, livro in enumerate(livros, start=1):
        print(f"{i}. {livro['titulo']}")
        print(f"   Autor: {livro['autor']}")
        print(f"   Ano: {livro['ano']} | Páginas: {livro['paginas']}")
        print("-" * 40)

def remover_livro():

    if not livros:
        print("Nenhum livro cadastrado para remover.")
        return

    listar_livros()
    try:
        indice = int(input("Digite o número do livro que deseja remover: ")) - 1
        if indice < 0 or indice >= len(livros):
            print("Número inválido.")
            return
        livro_removido = livros.pop(indice)
        print(f"Livro '{livro_removido['titulo']}' removido com sucesso!")
    except ValueError:
        print("Erro: Digite um número válido.")

def ordenar_livros():

    if not livros:
        print("Nenhum livro cadastrado para ordenar.")
        return

    print("\nCritério de ordenação:")
    print("1. Ano de publicação")
    print("2. Número de páginas")
    print("3. Título (alfabético)")
    escolha = input("> ").strip()

    if escolha not in ["1", "2", "3"]:
        print("Opção inválida.")
        return

    ordem = input("Ordem (C para crescente, D para decrescente): ").strip().upper()
    reverse = ordem == "D"

    chaves = {"1": "ano", "2": "paginas", "3": "titulo"}
    chave = chaves[escolha]

    livros.sort(key=lambda x: x[chave], reverse=reverse)
    print(f"Livros ordenados por {chave} ({'decrescente' if reverse else 'crescente'}).")

def salvar_livros():

    try:
        with open("biblioteca.csv", "w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["titulo", "autor", "ano", "paginas"])
            for livro in livros:
                escritor.writerow([livro["titulo"], livro["autor"], livro["ano"], livro["paginas"]])
        print(f"Dados salvos com sucesso! ({len(livros)} livro(s))")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_livros():

    if not os.path.exists("biblioteca.csv"):
        print("Arquivo 'biblioteca.csv' não encontrado. Criando novo...")
        return

    try:
        with open("biblioteca.csv", "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)
            livros.clear()
            for linha in leitor:
                if len(linha) >= 4:
                    livros.append({
                        "titulo": linha[0],
                        "autor": linha[1],
                        "ano": int(linha[2]),
                        "paginas": int(linha[3])
                    })
        print(f"Dados carregados com sucesso! ({len(livros)} livro(s))")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def buscar_livros():

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    termo = input("Digite o termo de busca: ").strip().lower()
    if not termo:
        print("Termo de busca vazio.")
        return

    resultados = []
    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            resultados.append(livro)

    if resultados:
        print(f"\n{len(resultados)} resultado(s) encontrado(s):")
        for i, livro in enumerate(resultados, start=1):
            print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")
    else:
        print("Nenhum livro encontrado.")

def menu():

    carregar_livros()

    while True:
        print("\n" + "="*40)
        print("BIBLIOTECA DIGITAL")
        print("="*40)
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Remover livro")
        print("4. Ordenar livros")
        print("5. Buscar livros")
        print("6. Salvar dados")
        print("7. Sair")
        print("-" * 40)

        escolha = input("> ").strip()

        if escolha == "1":
            adicionar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            remover_livro()
        elif escolha == "4":
            ordenar_livros()
        elif escolha == "5":
            buscar_livros()
        elif escolha == "6":
            salvar_livros()
        elif escolha == "7":
            if livros:
                salvar = input("Deseja salvar os dados antes de sair? (S/N): ").strip().upper()
                if salvar == "S":
                    salvar_livros()
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()