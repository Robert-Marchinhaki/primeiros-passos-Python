from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar um nova pessoa', 'Sair do programa'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo.
        ler_arquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
