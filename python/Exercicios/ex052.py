# Sorteando um número de 0 a 100 e dizendo se ele é primo ou não

from random import randint
num = randint(0, 100)              # int(input('Digite um número: '))
print(f'Numero sorteado foi {num}')
for n in range(num-1, num, num):
    if num % 2 == 0 and num != 2 or num % 3 == 0 and num != 3:
        print('Não é primo.')
    elif num / 1 and num / num:
        print('É primo')
