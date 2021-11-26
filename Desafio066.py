n = c = s = 0
while True:
    n = int(input('Digite um numero a ser interado [999 pra sair] '))
    if n == 999:
        break
    s += n
    c += 1
print(f'\nA soma dos {c} números é {s}')
print('Fim do programa!')
