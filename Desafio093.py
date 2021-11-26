jogador = dict()
total = 0

jogador['nome'] = str(input('Digite o nome do jogador: '))
qnt_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
jogador['gols'] = list()
for c in range (1, qnt_partidas + 1):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c}: ')))
for c in jogador['gols']:
    total += c
jogador['total'] = total
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*20)
print(f'O jogador {jogador["nome"]} jogou {qnt_partidas} jogos')
for c, v in enumerate(jogador['gols']):
    print(f'na partida {c + 1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')