cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
    cor = input("Digite o nome de uma cor: ").lower()
    print(f"RGB da cor {cor}: {cores[cor]}")

except KeyError:
    print("Erro: Cor não encontrada no dicionário.")
    