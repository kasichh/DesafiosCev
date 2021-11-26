lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))

    if c == 0:
        lista.append(n)
        print(f'{n} abriu os valores da lista')
    elif n > lista[-1]:
        lista.append(n)
        print(f'{n} foi adicionado na última posição')
    else:
        i = 0
        while i < len(lista):
            if n <= lista[i]:
                lista.insert(i, n)
                break
            i += 1
        print(f'{n} foi adicionado na posição {i}')
print(lista)