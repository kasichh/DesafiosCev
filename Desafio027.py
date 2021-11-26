nome = str(input('Digite seu nome: ')).strip()
corte = nome.split()
last = len(corte)

print(f'Primeiro nome: {corte[0]}')
print(f'Último nome: {corte[last - 1]}')

