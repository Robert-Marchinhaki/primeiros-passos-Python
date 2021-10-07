# JOKENPÔ

'''from random import choice
from time import sleep
print('Vamos brincar de pedra, papel ou tesoura. Tente me vencer.')
print('pedra, papel, tesoura...')
sleep(3)
player1 = str(input('O que você escolheu? '))
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
print(f'Eu escolhi {computador}.')
if player1 == 'tesoura' and computador == 'papel':
    print('Você me venceu!')
elif player1 == 'tesoura' and computador == 'tesoura':
    print('Empatamos! A gente escolha a mesma coisa.')
elif player1 == 'tesoura' and computador == 'pedra':
    print('HAHA, eu venci!')
elif player1 == 'papel' and computador == 'papel':
    print('Empatamos! A gente escolheu a mesma coisa.')
elif player1 == 'papel' and computador == 'pedra':
    print('Você me venceu!')
elif player1 == 'papel' and computador == 'tesoura':
    print('HAHA, eu venci!')
elif player1 == 'pedra' and computador == 'pedra':
    print('Empatamos! A gente escolheu a mesma coisa.')
elif player1 == 'pedra' and computador == 'tesoura':
    print('Você me venceu!')
elif player1 == 'pedra' and computador == 'papel':
    print('HAHA, eu venci!')
else:
    print('ERROR')
    print('Verefique se o que você escreveu está dentro das possibilidades')'''

# EXERCICIO FEITO PELO PROFESSOR

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'\033[4;97;40m{"JOGUE DE ACORDO COM OS NÚMEROS ABAIXO!"}\033[m\n'
      '\n\033[1;35;40m[ 0 ] Pedra'
      '\n[ 1 ] Papel'
      '\n[ 2 ] Tesoura \n\033[m')
jogador = int(input('\033[4;97;40mFAÇA SUA JOGADA: '))
print('\033[31;40mJO')
sleep(1)
print('\033[33;40mKEN')
sleep(1)
print('\033[32;40mPO')
print('\033[m')
sleep(0.5)
print('\033[1;35;40m-=' * 15)
print(f'\nCOMPUTADOR JOGOU \033[34m{itens[computador]}')
print('\033[m\033[1;35;40m')
print(f'JOGADOR JOGOU \033[32m{itens[jogador]}')
print('\033[m\033[1;35;40m')
print('\033[1;35;40m-=' * 15, '\n\033[m')
if computador == 0:
    if jogador == 0:
        print('\033[1;33;40mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;32;40mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;34;40mCOMPUTADOR VENCEU!\033[m')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[1;34;40mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;33;40mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;32;40mJOGADOR VENCEU!\033[m')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[1;32;40mJOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;34;40mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;33;40mEMPATE!\033[m')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.\033[m')
