jogadores = []
tabela_jogador = {}
gols_partida = []

while True:
    nome = str(input('Nome: '))
    pt_jogadas = int(input(f'{nome}, quantas partidas você jogou? '))
    tabela_jogador['nome'] = nome

    if pt_jogadas != 0:
        total_gols = 0
        for c in range(0, pt_jogadas):
            gols_feitos = int(input(f'{nome}, quantos gols você fez na {c + 1}° partida? '))
            total_gols += gols_feitos
            gols_partida.append(gols_feitos)
            tabela_jogador['gols'] = gols_partida.copy()
        tabela_jogador['total'] = total_gols
        gols_partida.clear()
    jogadores.append(tabela_jogador.copy())
    tabela_jogador.clear()
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-='*22)
    while parada not in 'SN':
        print('Erro! Apenas [S/N]')
        parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
        print('-='*22)
    if parada in 'N':
        break

print(f'{"CÓD":<5}{"NOME":^5}{"GOLS":^15}{"TOTAL":>10}')
for pos, val in enumerate(jogadores):
    print(f'{pos:<5}{val["nome"]:^5}    {val["gols"]}{val["total"]:>10}')

print('-='*22)
while True:
    print('Digite o código do jogador desejado')
    dados = int(input('Mostrar dados de qual jogador? '))
    while dados > len(jogadores) or dados < 0:
        print('Erro! Esse jogador não existe.')
        dados = int(input('Mostrar dados de qual jogador? '))
    else:
        print(f'Levantamento do jogador {jogadores[dados]["nome"]}')
        for k, i in enumerate(jogadores):
            if k == dados:
                for c in range(0, len(i["gols"])):
                    print(f'    => No {c + 1}° jogo fez {i["gols"][c]} gols')
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-=' * 22)
    while parada not in 'SN':
        print('Erro! Responda apenas com [S/N]')
        parada = str(input('Quer continuar? [S/N]:')).upper().strip()
        print('-=' * 22)
    if parada in 'N':
        break
print(jogadores)
