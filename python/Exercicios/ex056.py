# ANALISADOR COMPLETO
soma = 0
mih = 0
nhm = ''
mv = 0

for p in range(1, 5):
    print(f'-------- {p}° PESSOA --------')
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    idade = int(input('Idade: '))
    soma += idade
    if p == 1 and sexo == 'M':
        mih = idade
        nhm = nome
    if sexo == 'M' and idade > mih:
            mih = idade
            nhm = nome
    if sexo == 'F' and idade < 20:
        mv += 1
print(f'Ao todo {mv} mulher(es) tem menos de 20 anos')
print(f'O homem com a maior idade é {nhm}')
print(f'A média de idade do grupo é {soma / 4:.1f}')
