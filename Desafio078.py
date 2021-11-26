lista = list()

for c in range(1, 6):
    lista.append(int(input(f'Digite o {c} valor: ')))

print(f'A lista que voce digitou foi {lista}')

#MAIOR VALOR
# print(f'O maior valor é: {max(lista)} e está na posição {lista.index(max(lista))+1}')
print(f'O maior valor é: {max(lista)}, e está na posição ',end='')
for n, m in enumerate(lista):
    if m == max(lista):
        print(n+1,end='...')

#MENOR VALOR
# print(f'\nO menor valor é: {min(lista)} e está na posição {lista.index(min(lista))+1}')
print(f'\nO menor valor é {min(lista)}, e está na posição ', end='')
for o, p in enumerate(lista):
    if p == min(lista):
        print(o+1, end='...')
