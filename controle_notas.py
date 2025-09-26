# Exercício 1 - Controle de Notas

nome = input("Digite o nome do aluno: ")
notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"\nAluno: {nome}")
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado ✅")
else:
    print("Situação: Reprovado ❌")
