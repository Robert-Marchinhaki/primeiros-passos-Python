def confirmar(stop=False):
    """
    :param stop: False por padrão, caso seja True vai parar o outro programa
    :return: returna a parada para dar break
    """
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while parada not in 'SN':
        parada = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if parada in 'S':
        ...
    else:
        return parada


def turma(situacao=False):
    """
    :param situacao: False para não mostrar a situação do aluno ou True para mostrar a situação do aluno
    :return: sem retorno
    """
    boletim = {}
    qtde_notas = somar_media = maior_nota = menor_nota = media_turma = 0
    while True:
        info_notas = float(input('Informe suas notas: '))
        qtde_notas += 1
        somar_media += info_notas
        if qtde_notas == 1:
            maior_nota = menor_nota = info_notas
        if maior_nota < info_notas:
            maior_nota = info_notas
        if menor_nota > info_notas:
            menor_nota = info_notas
        boletim['notas'] = qtde_notas
        boletim['maior nota'] = maior_nota
        boletim['menor nota'] = menor_nota
        if confirmar(stop=False):
            break
    media_turma = somar_media / qtde_notas
    boletim['media'] = media_turma
    if situacao:
        if boletim['media'] > 7:
            boletim['situacao'] = 'APROVADO'
        elif boletim['media'] > 6:
            boletim['situacao'] = 'RECUPERAÇÃO'
        else:
            boletim['situacao'] = 'REPROVADO'
    print(boletim)


while True:
    mostrar_situacao = str(input('Quer mostrar a situação do aluno? [S/N]: ')).upper().strip()[0]
    if mostrar_situacao not in 'SN':
        print('Informe apenas [S/N]')
        mostrar_situacao = str(input('Quer mostrar a situação do aluno? [S/N]: ')).upper().strip()[0]
    if mostrar_situacao == 'S':
        mostrar_situacao = True
    else:
        mostrar_situacao = False
    if mostrar_situacao == False or True:
        break

turma(situacao=mostrar_situacao)

