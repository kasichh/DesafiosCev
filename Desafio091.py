import random
jogadores = dict()
from operator import itemgetter

for c in range (1, 5):
    valor = random.randint(1, 6)
    jogadores[f'Jogador{c}'] = valor

ranking = list()

print('Valores sorteados')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} tirando {v[1]}')