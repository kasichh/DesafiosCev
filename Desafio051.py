p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
s = 0

for c in range(0, 10, 1):
    print(f'O {c + 1:2} termo é {p}')
    p += r
    s = s + p
print(f'A soma da PA é {s}!')