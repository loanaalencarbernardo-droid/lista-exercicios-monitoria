# Exercício 6 - Estatísticas de Vendas

vendas = {
    "Janeiro": 1200,
    "Fevereiro": 950,
    "Março": 1430
}

total = sum(vendas.values())
media = total / len(vendas)
maior_mes = max(vendas, key=vendas.get)
menor_mes = min(vendas, key=vendas.get)

print("--- Estatísticas de Vendas ---")
print(f"Total de vendas: R$ {total}")
print(f"Média mensal: R$ {media:.2f}")
print(f"Mês com maior venda: {maior_mes} (R$ {vendas[maior_mes]})")
print(f"Mês com menor venda: {menor_mes} (R$ {vendas[menor_mes]})")
