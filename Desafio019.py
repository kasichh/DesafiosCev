import random

# a = 'Pedro'
# b = 'Ariadne'
a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto nome: ')

nome = random.choice([a, b, c, d])

print(f'O sorteado é: {nome}!')
