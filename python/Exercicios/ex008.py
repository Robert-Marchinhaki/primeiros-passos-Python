# CONVERSOR DE METRO PARA OUTROS TIPOS DE MEDIDAS

mt = float(input('Digite um valor (metro):'))
km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10
cm = mt * 100
mm = mt * 1000
print(f'\n {mt}M equivale a {km}km.\n {mt}M equivale a {hm}hm.\n {mt}M equivale a {dam}dam.\n {mt}M equivale a {dm}dm'
      f'\n {mt}M equivale a {cm}cm.\n {mt}M equivale a {mm}mm.')