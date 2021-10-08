# TENTANDO ADVINHAR UM NÚMERO V 2.0 (EX028)

from random import randint
computador = randint(1, 10)
jogador = int(input('Tente acertar o número que o computador escolheu: '))
contador = 1
while jogador != computador:
    jogador = int(input('Errou. Tente denovo: '))
    contador += 1
    if jogador == computador:
        print('...')
    else:
        if jogador < computador:
            print('DICA: mais')
        elif jogador > computador:
            print('DICA: menos')
if jogador == computador:
    if contador == 1:
        print('Parabéns, você acertou de primeira')
    elif contador <= 5:
        print('Seu desempenho foi mediano')
    else:
        print('Você teve muita dificuldade')
print(f'O número que o computador escolheu foi: {computador}\n'
      f'Você precisou realizar {contador} jogada(s) para acertar.')