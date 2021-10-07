# ALTERANDO O JEITO COMO O NOME FOI ESCRITO

nome = str(input('Digite seu nome: '))
nomemais = nome.upper()
nomemin = nome.lower()
nometot = nome.split()
nomeum = len(nometot[0])
nomel = len(nome.replace(" ", ""))

print(f'\n seu nome com todas letras maiusculas ficara assim: {nomemais}'
     f'\n seu nome com todas letras minusculas ficara assim: {nomemin}'
     f'\n seu primeiro nome tem um total de {nomeum} letras'
     f'\n seu nome inteiro tem um total de {nomel} letras')


'''nome = str(input('Digite seu nome: ')).strip()
print(f'\n Seu nome em maiúsculas é {nome.upper()}.'
      f'\n Seu nome em minúsculas é {nome.lower()}.'
      f'\n Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.'
      f'\n Seu primeiro nome tem {nome.find(" ")} letras.')
'''
