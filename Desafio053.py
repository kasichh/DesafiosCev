texto = str(input('Teste de palíndromo: ')).strip().replace(' ', '').lower()
lista = []
lista = list(texto)
atsil = []

cont = len(lista)

for c in range(cont, 0, -1):
    atsil.append(lista[c-1])

juntonormal = ''.join(lista)
juntocontrario = ''.join(atsil)
print(f'{juntonormal} ao contrário fica {juntocontrario}')

if atsil == lista:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
