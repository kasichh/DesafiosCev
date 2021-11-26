a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))

numeros = (a, b, c, d)

print(f'Você digitou os valores: {sorted(numeros)}')

nove = 0
for c in numeros:
    if c == 9:
        nove += 1
if nove>0:
    print(f'O valor 9 apareceu {nove} vez(es)')
else:
    print('O número 9 não apareceu nenhuma vez!')

tres = 0
for c in numeros:
    if c == 3:
        tres += 1
if tres>0:
    print(f'O valor 3 apareceu {tres} vez(es)')
else:
    print('O número 3 não apareceu nenhuma vez!')

print('Os valores pares digitados foram ', end='')
for c in numeros:
    if c%2 == 0:
        print(c,end=' ')
