def voto():
    from datetime import datetime
    nascimento = int(input('Informe o ano de nascimento: '))
    while nascimento > datetime.now().year:
        print('Erro! O ano de nascimento não pode exceder o ano atual.')
        nascimento = int(input('Digite novamente: '))
        if nascimento < datetime.now().year:
            break
    idade = datetime.now().year - nascimento
    if idade > 65 or 15 < idade < 18:
        return print(f'Com {idade} anos: Votar é opcional.')
    elif idade >= 18:
        return print(f'Com {idade} anos: Votar é obrigatório.')
    else:
        return print(f'Com {idade} anos: Não é permitido votar.')


voto()
