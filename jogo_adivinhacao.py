# Exercício 5 - Jogo de Adivinhação

import random

numero_secreto = random.randint(1, 20)
tentativas = []

print("🎲 Adivinhe o número entre 1 e 20!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas.append(palpite)

    if palpite == numero_secreto:
        print(f"\nParabéns! Você acertou em {len(tentativas)} tentativas.")
        print("Seus palpites foram:", tentativas)
        break
    elif palpite < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
