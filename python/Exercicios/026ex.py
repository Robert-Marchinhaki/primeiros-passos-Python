# VERIFICANDO QUANTAS E ONDE A LETRA 'A' APARECE EM UMA FRASE

frase = input('Digite uma frase: ')
vezesa = frase.count('a')
popri = frase.find('a')
proul = frase.rfind('a')
print(f'\n Na sua frase a letra "a" aparece {vezesa} vezes.'
      f'\n Na sua frase a letra "a" aparece pela primeria vez na {popri}° posição.'
      f'\n Na sua frase a letra "a" aparece pela última vez na {proul}° posição.')