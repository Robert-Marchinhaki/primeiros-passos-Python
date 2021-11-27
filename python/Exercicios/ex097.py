def mensagem(num, txt):
    print('-' * (num + 2))
    print('', txt)
    print('-' * (num + 2))


frase = str(input('Digite sua frase: ')).strip()
mensagem(num=len(frase), txt=frase)
