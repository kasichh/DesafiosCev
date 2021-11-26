p = int(input('O primeiro termo da PA vale: '))
r = int(input('A razão da PA vale: '))
c = 1
cont = 0

while c < 11:
    print(f'O {c:2} termo da PA vale {p}')

    p += r
    c += 1

termos = -1

cont = c - 1
p -= r

while termos != 0:
    i = 1
    termos = int(input('\nQuer ver mais quantos termos?[0 para finalizar] '))
    while i < (termos+1):
        p += r
        cont += 1

        print(f'O {cont} termo vale {p}')

        i += 1
print(f'\nContador de PA finlizado com {cont} termos mostrados!')
