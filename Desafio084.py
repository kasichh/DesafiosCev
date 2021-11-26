galera = []
pessoa = []
pesadas = []
leves = []
i = maior_peso = menor_peso = 0
continua = ''

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))

    if galera == []:
        maior_peso = pessoa[1]
        menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            pesadas.clear()
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            leves.clear()
            menor_peso = pessoa[1]

    i += 1
    if pessoa[1] >= maior_peso:
        pesadas.append(pessoa[0])
    if pessoa[1] <= menor_peso:
        leves.append(pessoa[0])

    galera.append(pessoa[:])
    pessoa.clear()

    continua = str(input('Deseja continuar?[S/N] '))

    if continua in 'Nn':
        break

print(galera)
print(f'Foram {i} nomes!')
print(f'As mais leves pesam {menor_peso},são: ', end='')
for c in leves:
    print(c, end=' ')
print(f'\nAs mais pesadas pesam {maior_peso}, são: ',end='')
for c in pesadas:
    print(c,end=' ')
