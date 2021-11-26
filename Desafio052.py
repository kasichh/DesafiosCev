p = int(input('Digite um número e teste se ele é primo: '))
t = p - 1
n_primo = 0

for t in range(t, 1, -1):
    if p % t == 0:
        n_primo = 1

if n_primo == 1:
    print(f'O número {p} \033[1;31mnão é primo!\033[m')
else:
    print(f'O número {p} \033[1;32mé primo!\033[m')
