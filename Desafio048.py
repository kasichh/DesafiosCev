s = 0
contagem = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        print(c)
        s += c
        contagem += 1
print(f'A soma dos {contagem} valores é {s}!')
