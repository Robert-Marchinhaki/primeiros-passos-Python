# SIMULADOR DE CAIXA ELETRÔNICO

valorsacar = int(input('Valor a ser sacado: '))

total = valorsacar
nota = 50
totalnotas = 0

while True:
    if total >= nota:
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Você recebeu {totalnotas} nota(s) de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnotas = 0
        if total == 0:
            break
print('Volte sempre')
