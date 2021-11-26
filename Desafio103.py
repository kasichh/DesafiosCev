def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato!')

ficha(str(input('Nome do jogador: ')), str(input('Quantidade de gols: ')))
