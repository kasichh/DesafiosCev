listagem = ('Pão', 1, 'Leite', 3.50, 'Café', 5, 'Arroz', 10)

print('-'*20)
print('Listagem de preços')
print('-'*20)

for c in range (0, len(listagem), 2):
    b = c+1
    print(f'{listagem[c]}........... R${listagem[b]}')
print('-'*20)