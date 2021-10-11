# JOGO DO PAR OU ÍMPAR

from random import randint
from time import sleep

print('-='*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*12)

t = cont = 0

while True:
    c = randint(1, 10)
    n = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar[P/I]? ')).upper().strip()[0]
    t = c + n
    if t % 2 == 0 and e == 'P':
        print('-' * 20)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {t} é PAR')
        print('-' * 20)
        sleep(1)
        print('↓' * 15)
        print('Você ganhou!')
        print('↑' * 15)
        sleep(1)
    elif t % 2 != 0 and e == 'I':
        print('-' * 20)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {t} é ÍMPAR')
        print('-' * 20)
        sleep(1)
        print('↓' * 15)
        print('Você ganhou!')
        print('↑' * 15)
        sleep(1)
    elif t % 2 == 0 and e == 'I':
        print('-' * 20)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {t} é PAR')
        print('➶' * 15)
        sleep(1)
        print('↓' * 15)
        print('Você perdeu!')
        print('↑' * 15)
        sleep(1)
        break
    elif t % 2 != 0 and e == 'P':
        print('-' * 20)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {t} é ÍMPAR')
        print('-' * 20)
        sleep(1)
        print('↓' * 15)
        print('Você perdeu!')
        print('↑' * 15)
        sleep(1)
        break
    cont += 1
print(f'GAMER OVER! Você venceu {cont} vezes.')