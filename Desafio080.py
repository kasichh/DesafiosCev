lista = list()
valor = int(0)
lugar_adicionado = []

for c in range (0, 5):
    lista.append(int(input('Digite um valor: ')))

    if c == 0:
        print(f'O valor {lista[0]} foi adionado na posição 0')
    for d in range(0, len(lista)-1):
        if lista[-1]<lista[d]:
            lista.insert(d, lista[-1])
            print(f'O valor {lista[-1]} foi adicionado na posição {d}')
            lista.pop()
            break

print(f'\nA lista digitada foi: {lista}')