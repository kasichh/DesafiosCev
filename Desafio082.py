lista = list()
pares = list()
impares = list()
continua = 'x'

while True:
    lista.append(int(input('Digite um número: ')))

    continua = 'x'

    while continua not in 'SN':
        continua = str(input('Deseja continuar?[S/N]')).upper().strip()[0]

    if continua == 'N':
        break


for c in lista:
    if c%2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'A lista é {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valroes impares são {impares}')