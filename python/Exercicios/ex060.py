# NÚMEROS FATORIAIS

# n = int(input('Digite um número: '))
#
# res = 1
# ini = 1
#
# while ini <= n:
#     res *= ini
#     ini += 1
# print(res)

n = int(input('Digite um número: '))
s = 1
for n in range(n, 0, -1):
    s *= n
print(s)