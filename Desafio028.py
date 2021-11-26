import random
import time
# r = [0, 1, 2, 3, 4, 5]
# a = random.choice(r)
a = random.randint(0, 5)

tent = int(input('Tenta acertar o valor de 0 a 5: '))
print('Processando...')
time.sleep(2)

if tent == a:
    print('Parabéns você acertou!')
else:
    print('Errou')
    print(f'O valor era: {a}')
