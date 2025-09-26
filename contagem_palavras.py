# Exercício 3 - Contagem de Palavras

frase = input("Digite uma frase: ")
palavras = frase.split()
contagem = {}

for palavra in palavras:
    palavra = palavra.lower()
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("\nDicionário de contagem de palavras:")
print(contagem)
