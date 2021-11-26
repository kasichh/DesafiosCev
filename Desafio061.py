p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i = 1
soma = 0

while i < 11:
    print(f'o {i:2} termo da PA vale {p}')

    soma += p
    p += r

    i += 1
print(f'\nA soma da PA vale: {soma}')
