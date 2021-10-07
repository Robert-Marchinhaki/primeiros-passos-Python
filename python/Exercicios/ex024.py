# VERIFICADOR DE CIDADE

cidade = input('Digite o nome da sua cidade: ').strip()
quebrar = cidade.split()
verificar = 'SANTO' in quebrar[0].upper()
print(f'Verificando se sua cidade começa com Santo... {verificar}')
