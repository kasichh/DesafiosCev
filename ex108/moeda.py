def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')


def metade(num='0'):
    return num / 2


def dobro(num=0):
    return num*2


def aumentar(num=0, perc=0):
    return num*(1 + (perc / 100))


def reduzir(num=0, perc=0):
    return num*(1 - (perc/100))


