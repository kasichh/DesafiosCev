sal = float(input('Digite seu salário: R$ '))

if sal > 1250:
    print(f'O salário ajustou para: {sal*1.1:.2f}')
else:
    print(f'O salário ajustou para: {sal*1.15:.2f}')
