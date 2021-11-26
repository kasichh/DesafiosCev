s = 0
cont = 0
for c in range(0,6):
    v = int(input('Digite um valor inteiro, se for par será interado! '))
    if (v % 2) == 0:
        s += v
        cont += 1

print(f'A soma dos {cont} valores pares é: {s}')
