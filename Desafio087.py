matriz = [[], [], []]
valor = pares = seg_col = cont = terc = 0


for c in range(0,3):
    for d in range(0,3):
        valor = int(input(f'[{c}] [{d}]: '))
        matriz[c].append(valor)

print('=-'*20)

for e in matriz:
    for f in e:
        print(f'[{f:^5}] ', end='')
    print()

print('=-'*20)

for e in matriz:
    cont = 0
    for f in e:
        if f%2 == 0:
            pares += f
        if cont == 2:
            terc += f
        cont += 1

print(f'A soma dos números pares é: {pares}')
print(f'A soma dos números da segunda coluna é: {terc}')
print(f'O mair valor da segunda linha é: {max(matriz[1])}')
