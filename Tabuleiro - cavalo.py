# Criei uma lista vazia chamada "tabuleiro"
# Ela irá armazenar as 8 linhas do tabuleiro de xadrez
tabuleiro = []

# Laço para criar as 8 linhas do tabuleiro
for i in range(8):

    # Cada linha começa como uma lista vazia
    linha = []

    # Laço para adicionar 8 colunas na linha
    for j in range(8):

        # Adiciona "." para representar uma casa vazia
        linha.append(".")

    # Depois de completar a linha com 8 posições,
    # adiciona essa linha ao tabuleiro
    tabuleiro.append(linha)

# Pede ao usuário para inserir a linha onde o cavalo será colocado
# O valor deve estar entre 0 e 7
linha = int(input("Digite a linha do cavalo (0 a 7): "))

# Pede ao usuário para inserir a coluna onde o cavalo será colocado
# O valor também deve estar entre 0 e 7
coluna = int(input("Digite a coluna do cavalo (0 a 7): "))

# Verifica se a posição digitada é inválida
# Se a linha ou coluna estiver fora do intervalo 0-7,
# mostra uma mensagem de erro
if linha < 0 or linha > 7 or coluna < 0 or coluna > 7:
    print("Posição inválida!")

# Caso a posição seja válida
else:

    # Lista com todos os movimentos possíveis do cavalo
    # Cada tupla representa:
    # (movimento nas linhas, movimento nas colunas)
    movimentos = [
        (-2, -1), (-2, 1),   # 2 para cima e 1 para esquerda/direita
        (-1, -2), (-1, 2),   # 1 para cima e 2 para esquerda/direita
        (1, -2),  (1, 2),    # 1 para baixo e 2 para esquerda/direita
        (2, -1),  (2, 1)     # 2 para baixo e 1 para esquerda/direita
    ]

    # Cola a letra "C" na posição escolhida
    # para representar o cavalo
    tabuleiro[linha][coluna] = "C"

    # Percorremos cada movimento possível do cavalo
    for mov in movimentos:

        # Calcula a nova linha somando
        # a posição atual com o movimento
        nova_linha = linha + mov[0]

        # Calcula a nova coluna
        nova_coluna = coluna + mov[1]

        # Verifica se a nova posição ainda está dentro do tabuleiro
        # Isso evita acessar posições inexistentes
        if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:

            # Marcamos a posição possível do cavalo com "*"
            tabuleiro[nova_linha][nova_coluna] = "*"

    # Exibimos o tabuleiro final
    print("\nTabuleiro:")

    # Percorremos cada linha do tabuleiro
    for l in tabuleiro:

        # join() junta os elementos da lista com espaço entre eles
        # deixando o tabuleiro organizado na hora de imprimir
        print(" ".join(l))






