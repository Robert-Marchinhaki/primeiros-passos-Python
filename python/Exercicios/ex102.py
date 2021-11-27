def fatorial(num=1, show=False):
    """
    :param num: recebe um número inteiro e mostra o calcúlo do seu fatorial
    :param show: mostra o passo a passo de como o calcúlo foi feito
    :return: retorna o resultado (fatorial do número informado)
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print('x', end='')
            print(f' {c} ', end='')
    print('= ', end='')
    return f


fatoriando = int(input('Informe um número: '))
print(""" A seguir Você poderá informar a opções que deseja.
[ 1 ]   Informando o número 1 você mostrará o calcúlo da conta
[ 2 ]   Informando o número 2 você optará por não mostrar o calcúlo
[ 3 ]   Informando o número 3 você poderá acessar o help da função
""")
while True:
    quero_ajuda = False
    mostrar_calculo = int(input('Opções: '))
    if mostrar_calculo == 1:
        mostrar_calculo = True
    elif mostrar_calculo == 2:
        mostrar_calculo = False
    elif mostrar_calculo == 3:
        quero_ajuda = True
    else:
        print('Só temos 3 opções: 1, 2 ou 3.')
    if mostrar_calculo == True or mostrar_calculo == False or quero_ajuda == True:
        break

print(f'{fatorial(fatoriando, show=mostrar_calculo)}')
if quero_ajuda:
    help(fatorial)
