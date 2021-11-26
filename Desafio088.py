from random import randint
from time import sleep

jogos = []
jogo = []
qnt_jogos = numero = 0

print('='*30)
print(f'{"JOGAR NA MEGA SENA":^30}')
print('='*30)

qnt_jogos = int(input('Quantos jogos quer sortear?: '))

for c in range(0, qnt_jogos):
    while True:
        numero = randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)
            jogo.sort()
        if len(jogo) == 6:
            break
    jogos.append(jogo[:])
    jogo.clear()
print(f'=-'*3, f'   SORTEANDO {qnt_jogos} JOGOS   ', '-='*3)
for c in range(0, qnt_jogos):
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(0.5)
print('=-'*5, 'BOA SORTE', '-='*5)
