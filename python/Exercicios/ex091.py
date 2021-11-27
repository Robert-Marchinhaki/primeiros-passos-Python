from random import randint
from operator import itemgetter
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
for k, i in jogos.items():
    print(f'{k} jogou {i}')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for k, i in enumerate(ranking):
    print(f'{i[0]} ficou em {k + 1}° lugar')
