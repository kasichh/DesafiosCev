import datetime
i = 0
ano = datetime.date.today().year

for c in range(0,7):
    a = int(input(f'Qual o {c+1} ano de nascimento? '))
    if (ano - a) > 18:
        i += 1

if i > 1:
    print(f'Nessas pessoas, {i} são maiores de idade!')
if i < 7:
    print(f'Sendo assim, {7 - i} são menores de idade!')
