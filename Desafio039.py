import datetime

a = datetime.date.today()
a = str(a)
b = (a[:4])
b = int(b)

nasc = int(input('Qual seu ano de nascimento? '))
idade = (b - nasc)

print(f'Quem nasceu em {nasc} tem {idade} anos')

if idade < 18:
    print('Você ainda vai se inscrever no alistamento.')
    print(f'Ainda faltam {18 - idade} anos')
    print(f'Seu alistamento será em {b + (18-idade)}')
elif idade > 18:
    print('Você já passou dessa fase.')
    print(f'E ja fazem {idade - 18} anos')
    print(f'Foi em {b - (idade - 18)}')
else:
    print('Esse ano voce deve se alistar.')
