def pergunta(stop=False):
    while True:
        mostrar_calculo = int(input('Informe [1] para continuar , ou [2] para para parar: '))
        if mostrar_calculo == 1:
            mostrar_calculo = True
        elif mostrar_calculo == 2:
            mostrar_calculo = False
        else:
            print('Erro! Informe somente [1] ou [2].')
        if not mostrar_calculo:
            break


pergunta(stop=False)
