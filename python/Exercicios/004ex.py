# VERFICANDO UM PALAVRA OU NÚMERO

n = input('Digite qualquer coisa:')
print(f'é um número? {n.isnumeric()}')
print(f'tem espaço? {n.isspace()}')
print(f'tem letras? {n.isalpha()}')
print(f'É alpha numérico? {n.isalnum()}')
print(f'Está em maisculo? {n.isupper()}')
print(f'Está em minusculo? {n.islower()}')

