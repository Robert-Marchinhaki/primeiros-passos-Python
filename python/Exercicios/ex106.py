def helping():
    while True:
        phrase0 = ' SISTEMA DE AJUDA DO PyHELP '
        print(phrase0)
        print('-'*len(phrase0))
        phrase1 = ' Digite (fim) para parar o programa '
        print(phrase1)
        print('-'*len(phrase1))
        my_help = str(input('Função ou biblioteca > \033[7;35m')).lower()
        if my_help in 'fim':
            phrase_end = ' VOLTE SEMPRE QUE PRECISAR. '
            print('-'*len(phrase_end), )
            print(f'{phrase_end}')
            print('-'*len(phrase_end))
            break
        print('...')
        phrase2 = f' Acessando o manual do comando {my_help} '
        print('&'*len(phrase2))
        print(phrase2)
        print('&'*len(phrase2))
        print('\33[m')
        print('\033[7m')
        help(f'{my_help}')
        print('\033[m')


helping()
