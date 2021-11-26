import random

a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')

lista = random.sample([a, b, c, d], k=4)

for palavra in lista:
    print(palavra, end=' ')
