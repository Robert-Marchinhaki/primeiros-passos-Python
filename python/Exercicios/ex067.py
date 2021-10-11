# TABUADA V 3.0

while True:
    n = int(input('Quer ver a tabuda de qual valor? '))
    print('-'*30)
    if n <= -1:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for x in range(1, 11):
        print(f'{n} x {x} = {n * x}')
    print('-' * 30)
