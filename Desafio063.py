primeiro_termo = 0
segundo_termo = 1
i = 1
fib = 0
n = int(input('Quer ver quantos termos de Fibonacci: '))
print(f'{primeiro_termo}', end='')
while i < n:
    fib = primeiro_termo + segundo_termo
    print(f'→{fib}', end='')
    if i % 2 == 0:
        primeiro_termo = fib
    else:
        segundo_termo = fib
    i += 1
print('\n\nCabo PORRA')

