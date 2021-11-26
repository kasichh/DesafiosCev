sexo = str(' ')
while not sexo in 'MmFf':
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if sexo not in 'MmFf':
        print('Digite um sexo válido!')

print(f'Sexo registrado : {sexo}')
