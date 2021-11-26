num = 0
quantidade = 0
continua = 'S'
maior = 0
menor = 0
soma_valores = 0

while continua == 'S':
    num = int(input('Digite um valor: '))

    soma_valores += num

    if quantidade == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    quantidade += 1

    continua = input('Deseja continuar o programa? [S/N]').strip().upper()

print(f'A média dos {quantidade} valores é: {soma_valores/quantidade}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
