def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')


def metade(num=0, format=False):
    valor = num / 2
    if format:
        return moeda(valor)
    else:
        return valor


def dobro(num=0, format=False):
    valor = num*2
    if format:
        return moeda(valor)
    else:
        return valor


def aumentar(num=0, perc=0, format=False):
    valor = num*(1 + (perc / 100))
    if format:
        return moeda(valor)
    else:
        return moeda


def reduzir(num=0, perc=0, format=False):
    valor = num*(1 - (perc/100))
    if format:
        return moeda(valor)
    else:
        return valor


