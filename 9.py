vendas_dia = {"Notebook": "2500", "Mouse": 80, "Teclado": "150"}

def total_vendas(vendas):
    total = 0
    for produto, valor in vendas.items():
        try:
            total += float(valor)
        except (ValueError, TypeError):
            print(f"Valor inválido para {produto}: {valor}")
    return total

print("Total de vendas:", total_vendas(vendas_dia))