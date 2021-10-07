# PA

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
m = 5

termog = termo + (m - 1) * razao
for m in range(termo, razao * 10, razao):
    print(f'Os dez primeiros termos são {m}')