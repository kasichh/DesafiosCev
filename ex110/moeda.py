def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')


def metade(num=0, formato=False):
    valor = num / 2
    if formato:
        return moeda(valor)
    else:
        return valor


def dobro(num=0, formato=False):
    valor = num*2
    if formato:
        return moeda(valor)
    else:
        return valor


def aumentar(num=0, perc=0, formato=False):
    valor = num*(1 + (perc / 100))
    if formato:
        return moeda(valor)
    else:
        return moeda


def reduzir(num=0, perc=0, formato=False):
    valor = num*(1 - (perc/100))
    if formato:
        return moeda(valor)
    else:
        return valor


def resumo(valor, acresc, decresc):
    print('='*30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('='*30)
    n = moeda(valor)
    print(f'Preço analisado: {n:>13}')
    print(f'Dobro do preço: {dobro(valor, True):>14}')
    print(f'Metade do preço: {metade(valor, True):>13}')
    print(f'{acresc}% de acrescimo: {aumentar(valor, acresc, True):>12}')
    print(f'{decresc}% de decrescimo: {reduzir(valor, decresc, True):>11}')
    print('='*30)

