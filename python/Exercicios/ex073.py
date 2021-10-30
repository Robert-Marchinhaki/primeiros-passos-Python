tabelabrasileirao = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Bragantino', 'Corinthians',
                     'Internacional', 'Fluminense', 'Atlético-PR', 'Cuiabá', 'América-MG', 'Atlético-GO',
                     'São Paulo', 'Ceará SC', 'Bahia', 'Juventude', 'Santos', 'Sport Recife', 'Grêmio',
                     'Chapecoense')
print('='*20)
print(f'Lista de times do brasileirão: {tabelabrasileirao}')
print('='*20)
# Primeiros 5 colocados
print(f'Os 5 primeiros colocados são: {tabelabrasileirao[0:5]}')
print('='*20)
# Os últimos 4 colocados
print(f'Os últimos 4 colocados são {tabelabrasileirao[-4:]}')
print('='*20)
# Lista com os times em ordem alfabética
print(f'Em ordem alfabética: {sorted(tabelabrasileirao)}')
print('='*20)
# Em qual posição da tabela está o time da chapecoense
for posicao in range(19, len(tabelabrasileirao)):
    print(f'O chapecoense está na {posicao + 1}° colocação')
print('='*20)