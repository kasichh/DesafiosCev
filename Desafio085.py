lista = [[], []]

novo_valor = 0

for c in range (1,8):
    novo_valor = int(input(f'Digite o {c} valor: '))

    if novo_valor%2 == 0:
        lista[0].append(novo_valor)
    else:
        lista[1].append(novo_valor)

print(f'Os valores pares são : {sorted(lista[0])}')
print(f'Os valores impares são: {sorted(lista[1])}')
