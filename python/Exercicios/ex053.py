# Identificador de frases Palíndromas


print('Vamos ver se sua frase pode ser uma frase Palíndromo. Você pode usar espaços, no entanto'
      ', evite os acentos. Obrigado.\n')
frase = str(input('Digite uma frase: '))


cont = len(frase.replace(" ", ""))

# print(f'{cont}')
# print(f'{frasem}')
# print(f'{cort}')

if cont < 3:
      print('Escreva uma frase maior.')
elif frase.replace(" ", "") == frase[::-1].replace(" ", ""):
      print(f'A sua frase é {frase.replace(" ", "")} e o inverso dela fica {frase[::-1].replace(" ", "")}')
      print('Sua frase forma um palíndromo')
else:
      print(f'A sua frase é {frase.replace(" ", "")} e o inverso dela fica {frase[::-1].replace(" ", "")}')
      print('Sua frase não forma um palíndromo')
