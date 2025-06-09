#Beatriz Paulino
#11.04.25
#EX10

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativa = 0

    while True:
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        tentativa += 1

        if palpite < numero_secreto:
            print("O número é maior. Tente novamnete.")
        elif palpite > numero_secreto:
            print("O número é menor. Tente novamente.")
        else:
            print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativa} tentativa."')
            break

jogo_adivinhacao()
