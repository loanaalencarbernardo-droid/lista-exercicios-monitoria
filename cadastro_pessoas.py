# Exercício 4 - Cadastro de Pessoas

pessoas = []

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade: "))
    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)

if pessoas:
    media_idades = sum([p["idade"] for p in pessoas]) / len(pessoas)
    print("\n--- Cadastro Final ---")
    print(f"Número total de pessoas: {len(pessoas)}")
    print(f"Média das idades: {media_idades:.2f}")
else:
    print("Nenhuma pessoa cadastrada.")
