f = int(input('Digite um numero e saiba seu fatorial: '))
fatorial = 1

print(f'{f}! = ', end='')
while f > 0:
    print(f, end='')
    if f != 1:
        print('.', end='')
    fatorial *= f
    f -= 1
print(f' = {fatorial}')

'''
f = int(input('Digite um número pra saber seu fatorial: '))
print(f'{f}! = ', end='')
fatorial = 1

for f in range (f, 0, -1):
    print(f, end='')
    if f != 1:
        print('.', end='')
    fatorial *= f
print(f' = {fatorial}')
'''