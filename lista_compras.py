# Exercício 2 - Lista de Compras

compras = []

while True:
    item = input("Digite um item da lista (ou 'fim' para encerrar): ")
    if item.lower() == "fim":
        break
    compras.append(item)

print("\n--- Lista Final ---")
print(f"Quantidade de itens: {len(compras)}")
print("Itens em ordem alfabética:", sorted(compras))
