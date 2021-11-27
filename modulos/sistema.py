from python.cor import colors_python

grupo_pessoas = []
lst_pessoas = {}
print_op = f"""
               {colors_python.cores["ciano sublinhado"]}OPÇÕES:{colors_python.cores["limpa"]} 
    --------------------------------                          
    {colors_python.cores["azul"]}[ 1 ] - Ver pessoas cadastradas{colors_python.cores["limpa"]} 
    {colors_python.cores["amarelo"]}[ 2 ] - Cadastrar um nova pessoa{colors_python.cores["limpa"]}
    {colors_python.cores["verde"]}[ 3 ] - Sair do sistema{colors_python.cores["limpa"]}
    """


def cadastro():
    while True:
        try:
            nome = str(input('Nome: ')).strip().replace('.', '').replace(',', '')
            if nome.isnumeric() or nome == '':
                print('Digie um nome válido.')
            else:
                lst_pessoas['nome'] = nome
        except Exception as error:
            print(f'Digite um nome válido. {error.__class__}')
        while True:
            try:
                idade = int(input('Idade: '))
                lst_pessoas['idade'] = idade
                grupo_pessoas.append(lst_pessoas.copy())
                break
            except Exception as error:
                print(f'Digite um número inteiro válido. {error.__class__}')

        try:
            while True:
                try:
                    print(print_op)
                    opcoes = int(input('Sua opção: '))
                    print('-'*30)
                    if opcoes == 2 or opcoes == 3:
                        break
                    elif opcoes == 1:
                        print(f'{"NOME"}{"IDADE":>25}')
                        print('-'*30)
                        for k, v in enumerate(grupo_pessoas):
                            print(f'{v["nome"]:<20} {v["idade"]:>5}')
                        continue
                    else:
                        print('Não temos essa opção.')
                        continue
                except (ValueError, TypeError):
                    print('Não conseguimos processar o valor ou o tipo digitado')
                except KeyboardInterrupt:
                    print('Usuário interrompeu o programa')

            if opcoes == 2:
                continue
            else:
                break
        except Exception as error:
            print(f'Formato inválido. As opções são: [1], [2] ou [3]. {error.__class__}')


cadastro()
