# NUMEROS POR EXTENSO

numeroextenso = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eigh', 'nine', 'ten', 'eleven',
                 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                 'nineteen', 'twenty')

while True:
    numeros = int(input('Digite um número de 0 a 20: '))
    while numeros < 0 or numeros > 20:
        numeros = int(input('Erro! Digite um número de 0 a 20: '))
    if numeros >= 0:
        print(f'Em inglês o número {numeros} se lê {numeroextenso[numeros]}')
    resposta = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if resposta in 'N':
        break
