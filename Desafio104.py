def leiaint(texto):
    num = input(f'{texto}')
    while True:
        if num.isnumeric():
            break
        else:
            num = input('Digite um valor válido NUMÉRICO: ')
    return num

n = leiaint('Digite um valor: ')
print(f'Você digitou {n}')
