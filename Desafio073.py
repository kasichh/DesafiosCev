times = ('Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza',
'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG', 'Fluminense', 'Flamengo',
'Corinthians', 'Ceará', 'Internacional', 'Juventudo', 'Sport', 'Cuiabá',
'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio')

print(f'Lista de times: {times}')

print(f'Os primerios 5 colocados são: {times[:5]}')

print(f'Os últimos 4 colocados são: {times[-4:]}')

print(f'A ordem alfabética é: {sorted(times)}')

i = 0
while times[i] not in 'Chapecoense':
    i+= 1
print(f'Chapecoense está na posição {i+1}')