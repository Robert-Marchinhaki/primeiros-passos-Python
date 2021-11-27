tabela_jogador = {}
gols_marcados = []

nome = str(input('Nome: '))
tabela_jogador['nome'] = nome
partidas_jogadas = int(input(f'{nome}, quantas partidas você jogou? '))

print('-='*30)

for partidas in range(0, partidas_jogadas):
    qtde_gols = int(input(f'Quantos gols você fez na {partidas + 1}° partida? '))
    gols_marcados.append(qtde_gols)

print('-='*30)
tabela_jogador['gols feitos'] = gols_marcados
total_gols = 0

for g, f in enumerate(gols_marcados):
    total_gols += f
tabela_jogador['total'] = total_gols

print(tabela_jogador)
print('-='*30)

for k, i in tabela_jogador.items():
    print(f'{k}: {i}')

print('-='*30)
print(f'O jogador {nome} jogou {partidas_jogadas} partidas.')
for p, g in enumerate(gols_marcados):
    print(f'    => Na partida {p + 1} fez {g} gols')
print(f'O jogador marcou um total de {tabela_jogador["total"]} gols')
