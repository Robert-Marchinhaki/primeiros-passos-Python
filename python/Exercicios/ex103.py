def futebol(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome: '))
n_gols = str(input('Número de gols: '))
if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0
if jogador.strip() == '':
    futebol(gols=n_gols)
else:
    futebol(nome=jogador, gols=n_gols)

