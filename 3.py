import os
import csv

produtos = []

def adicionar_produto():

    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: O nome do produto não pode estar vazio.")
        return

    categoria = input("Categoria: ").strip()
    if not categoria:
        print("Erro: A categoria não pode estar vazia.")
        return


    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print(f"Aviso: O produto '{nome}' já existe no estoque.")
            atualizar = input("Deseja atualizar a quantidade deste produto? (S/N): ").strip().upper()
            if atualizar == "S":
                atualizar_quantidade_existente(produto)
            return

    while True:
        try:
            preco = float(input("Preço: R$ "))
            if preco <= 0:
                print("Erro: O preço deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Erro: Preço deve ser um número válido.")

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: Quantidade deve ser um número inteiro.")

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def atualizar_quantidade():

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    listar_produtos()
    try:
        indice = int(input("Digite o número do produto: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Produto inválido.")
            return
        atualizar_quantidade_existente(produtos[indice])
    except ValueError:
        print("Erro: Digite um número válido.")

def atualizar_quantidade_existente(produto):

    print(f"\nProduto: {produto['nome']}")
    print(f"Quantidade atual: {produto['quantidade']}")

    try:
        ajuste = int(input("Quantidade para ajustar (+ entrada, - saída): "))
        nova_quantidade = produto["quantidade"] + ajuste

        if nova_quantidade < 0:
            print(f"Erro: Quantidade insuficiente. Estoque atual: {produto['quantidade']}")
            return

        produto["quantidade"] = nova_quantidade
        print(f"Quantidade atualizada! Novo estoque: {nova_quantidade}")

        if nova_quantidade <= 5:
            print(f"⚠️  ALERTA: Estoque baixo para '{produto['nome']}'!")

    except ValueError:
        print("Erro: Digite um número válido.")

def editar_produto():

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    listar_produtos()
    try:
        indice = int(input("Digite o número do produto a editar: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Produto inválido.")
            return

        produto = produtos[indice]
        print(f"\nEditando: {produto['nome']}")
        print("(Deixe em branco para manter o valor atual)")

        novo_nome = input(f"Nome [{produto['nome']}]: ").strip()
        if novo_nome:
            produto['nome'] = novo_nome

        nova_categoria = input(f"Categoria [{produto['categoria']}]: ").strip()
        if nova_categoria:
            produto['categoria'] = nova_categoria

        try:
            novo_preco = input(f"Preço [R$ {produto['preco']:.2f}]: ").strip()
            if novo_preco:
                produto['preco'] = float(novo_preco)
        except ValueError:
            print("Preço inválido. Mantendo valor anterior.")

        print("Produto atualizado com sucesso!")

    except ValueError:
        print("Erro: Digite um número válido.")

def remover_produto():

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    listar_produtos()
    try:
        indice = int(input("Digite o número do produto a remover: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Produto inválido.")
            return

        produto = produtos[indice]
        confirmar = input(f"Confirma remoção de '{produto['nome']}'? (S/N): ").strip().upper()

        if confirmar == "S":
            produtos.pop(indice)
            print(f"Produto '{produto['nome']}' removido com sucesso!")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("Erro: Digite um número válido.")

def listar_produtos():

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    print("\n" + "="*70)
    print(f"{'Nº':<4} {'Nome':<20} {'Categoria':<15} {'Preço':>10} {'Qtd':>8} {'Total':>10}")
    print("-"*70)

    valor_total_estoque = 0
    for i, p in enumerate(produtos, start=1):
        total_item = p['preco'] * p['quantidade']
        valor_total_estoque += total_item
        alerta = " ⚠️" if p['quantidade'] <= 5 else ""
        print(f"{i:<4} {p['nome']:<20} {p['categoria']:<15} R${p['preco']:>8.2f} {p['quantidade']:>8} R${total_item:>8.2f}{alerta}")

    print("-"*70)
    print(f"{'VALOR TOTAL DO ESTOQUE:':<50} R${valor_total_estoque:>18.2f}")
    print("="*70)
    print("⚠️ = Estoque baixo (5 ou menos unidades)")

def ordenar_produtos():

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    print("\nOrdenar por:")
    print("1. Preço")
    print("2. Quantidade")
    print("3. Nome")
    chave_opcao = input("> ").strip()

    chaves = {"1": "preco", "2": "quantidade", "3": "nome"}
    if chave_opcao not in chaves:
        print("Opção inválida.")
        return

    chave = chaves[chave_opcao]
    ordem = input("Ordem (c) crescente ou (d) decrescente: ").strip().lower()
    reverse = ordem == 'd'

    produtos.sort(key=lambda x: x[chave], reverse=reverse)
    print(f"Produtos ordenados por {chave} ({'decrescente' if reverse else 'crescente'}).")

def buscar_produtos():

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    termo = input("Digite o termo de busca: ").strip().lower()
    if not termo:
        print("Termo de busca vazio.")
        return

    resultados = []
    for produto in produtos:
        if termo in produto["nome"].lower() or termo in produto["categoria"].lower():
            resultados.append(produto)

    if resultados:
        print(f"\n{len(resultados)} resultado(s) encontrado(s):")
        for i, p in enumerate(resultados, start=1):
            print(f"{i}. {p['nome']} ({p['categoria']}) - R${p['preco']:.2f} - Qtd: {p['quantidade']}")
    else:
        print("Nenhum produto encontrado.")

def salvar_estoque():

    try:
        with open("estoque.csv", "w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["nome", "categoria", "preco", "quantidade"])
            for p in produtos:
                escritor.writerow([p["nome"], p["categoria"], p["preco"], p["quantidade"]])
        print(f"Dados salvos com sucesso! ({len(produtos)} produto(s))")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def carregar_estoque():

    if not os.path.exists("estoque.csv"):
        print("Arquivo 'estoque.csv' não encontrado. Criando novo...")
        return

    try:
        with open("estoque.csv", "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)
            produtos.clear()
            for linha in leitor:
                if len(linha) >= 4:
                    produtos.append({
                        "nome": linha[0],
                        "categoria": linha[1],
                        "preco": float(linha[2]),
                        "quantidade": int(linha[3])
                    })
        print(f"Dados carregados com sucesso! ({len(produtos)} produto(s))")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")

def menu():

    carregar_estoque()

    while True:
        print("\n" + "="*40)
        print("SISTEMA DE GESTÃO DE ESTOQUE")
        print("="*40)
        print("1. Adicionar produto")
        print("2. Atualizar quantidade")
        print("3. Editar produto")
        print("4. Remover produto")
        print("5. Listar produtos")
        print("6. Ordenar produtos")
        print("7. Buscar produtos")
        print("8. Salvar dados")
        print("9. Sair")
        print("-" * 40)

        opcao = input("> ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_quantidade()
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            listar_produtos()
        elif opcao == "6":
            ordenar_produtos()
        elif opcao == "7":
            buscar_produtos()
        elif opcao == "8":
            salvar_estoque()
        elif opcao == "9":
            if produtos:
                resposta = input("Deseja salvar o estoque antes de sair? (S/N): ").strip().upper()
                if resposta == "S":
                    salvar_estoque()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Digite um número de 1 a 9.")

if __name__ == "__main__":
    menu()