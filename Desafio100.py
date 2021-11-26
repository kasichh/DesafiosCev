from random import randint
from time import sleep


def sorteio(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    sleep(1)
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[-1], end=' ')
        sleep(0.5)
    print()


def soma_pares(numeros):
    soma_valores = 0
    for valor in numeros:
        if valor%2 == 0:
            soma_valores += valor
    print(f'Somando os valores pares de {numeros}, temos {soma_valores}')


lista = list()

sorteio(lista)
soma_pares(lista)

