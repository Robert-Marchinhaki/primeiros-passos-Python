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


def leia_float(num):
    while True:
        try:
            num = float(input('Digite um número real: '))
            break
        except Exception as error:
            print(f'\033[31mERRO: digite um valor real válido. Erro de {error.__class__}\033[m')


leia_int('Número inteiro: ')