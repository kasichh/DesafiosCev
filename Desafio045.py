import time
from random import choice

print('=-'*6, 'JOKENPO', '=-'*6)
esc = str(input('PEDRA PAPEL OU TESOURA?\n')).strip().lower() # escolha do jogador

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!')
time.sleep(1)

a = ['Pedra', 'Papel', 'Tesoura']
b = choice(a) #escolha final do computador
print('=-'*17)
print(f'O computador escolheu: \033[32m{b}\033[m')
print(f'O jogador escolheu \033[32m{esc}\033[m')
b = b.lower()

if esc == b:
    print('EMPATE')
elif esc == 'pedra':
    if b == 'tesoura':
        print('Você venceu!')
    else:
        print('Você perdeu!')
elif esc == 'tesoura':
    if b == 'pedra':
        print('Você perdeu!')
    else:
        print('Você venceu!')
elif esc == 'papel':
    if b == 'pedra':
        print('Você venceu!')
    else:
        print('Você perdeu!')
else:
    print('A sua escolha não  foi reconhecida')
print('=-'*17)
