from random import randint


def maior(* num):
    m = 0
    for valor in num:
        if m < valor:
            m = valor
    print(f'Foi sorteado {len(num)} valores ao todo. O maior valor sorteado entre {num} é {m}')


for c in range(randint(0, 10), randint(10, 20)):
    maior(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
