def linhas(cor, txt):
    if pintar in cores:
        print(cores[pintar])
    print(txt)


cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'branco': '\033[30m',
         'roxo': '\033[35m',
         'verde': '\033[32m',
         'ciano': '\033[36m',
         'limpa': '\033[m',
         'preto e branco': '\033[7;30;m'}

pintar = str(input('Deseja pintar o seu texto com qual cor? ')).lower()
while pintar not in cores:
    pintar = str(input('Erro! Essa cor não existe. Tente novamente: '))
    if pintar in cores:
        break
texto = str(input('Digite seu texto: '))
linhas(cor=pintar, txt=texto)

