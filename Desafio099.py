def maior(*valor):
    for c in valor:
        print(c, end=' ')
    print()
    quantidade = len(valor)
    if quantidade != 0:
        print(f'quantidade: {quantidade}', end='')
        print(f' maior {max(valor)}')
    else:
        print(f'quantidade: 0', end='')
        print(f' maior 0')

maior(2, 3, 5, 4, 14, 2, 4, 5, 4)
maior(0, 3, 4, 5, 1)
maior()
