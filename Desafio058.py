import random
palpites = 0
r = 0
palpite = -1
r = random.randint(0, 10)

print('Tente acertar o numero de 0 a 10')
while palpite != r:

    palpite = int(input('Tente acertar o numero: '))
    palpites += 1
    if palpite > r:
        print('Menos... ', end='')
    elif palpite < r:
        print('Mais... ', end='')
    if palpite != r:
        print('Tente novamente!')

print(f'Parabéns, você acertou!, foram necessárias {palpites} tentativas!')
