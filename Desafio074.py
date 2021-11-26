import random

numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(n,end=' ')

print('')
print(f'O menor número sorteado foi {sorted(numeros)[0]}')
print(f'O maior número sorteado foi {sorted(numeros)[4]}')
