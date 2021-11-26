matriz = [[], [], []]
valor = 0

for c in range(0,3):
    for d in range(0,3):
        valor = int(input(f'[{c}] [{d}] '))
        matriz[c].append(valor)

print('=-'*20)

for e in matriz:
    for f in e:
        print(f'[{f:^5}]', end='')
    print()
