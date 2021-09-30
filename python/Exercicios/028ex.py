# TENTANDO ADVINHAR UM NÚMERO DE 0 A 5

from random import choice

num = int(input('Digite um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
sort = choice(lista)
if num == sort:
    print('PARABÉNS!!! Você acertou.')
else:
    print('Você errou. Tente novamente.')

# DESAFIO FEITO PELO PROFESSOR

# from random import randint
# from time import sleep
# computador = randint(0,5)
# print('Estou pensando em um número entre 0 e 5')
# jogador = int(input('Em que número eu pensei? '))
# print('PROCESSANDO...')
# sleep(1)
# if jogador == computador:
#     print('PARABÉNS! Você conseguiu me vencer!')
# else:
#     print(f'ERROU! Eu pensei no número {computador}')