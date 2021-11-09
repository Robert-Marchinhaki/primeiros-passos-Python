# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

galera = []



while True:
    nomeidade = [str(input('Digite os nomes: ')), int(input('Digite as idades: '))]
    galera.append(nomeidade[:])
    avaliar = str(input('Quer continuar [S/N]? ')).upper().strip()
    while avaliar not in 'SN':
        avaliar = str(input('Não entendi! Digite novamente [S/N]: ')).upper().strip()
    if avaliar in 'N':
        break

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

