from python.cor.colors_python import cores


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Digite um valor inteiro válido.\033[m')
        except (KeyboardInterrupt, EOFError):
            print(f'O úsuario parou o programa.')
            return 0
        else:
            return n


def linha(tam=42):
    return f'{cores["amarelo em negrito"]}-{cores["limpa"]}' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho(f'{cores["roxo em negrito"]}{"MENU PRINCIPAL":^42}{cores["limpa"]}')
    c = 1
    for item in lista:
        print(f'{cores["azul em negrito"]}{c} - {item}{cores["limpa"]}')
        c += 1
    print(linha())
    opc = leia_int('Sua opção: ')
    return opc
