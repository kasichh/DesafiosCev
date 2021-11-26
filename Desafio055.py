lista = []

for c in range(0,5):
    novo = float(input('Digite um peso: '))
    lista.append(novo)

lista = sorted(lista)

print(f'O menor peso é {lista[0]} e o maior é {lista[4]}')
