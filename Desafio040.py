n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1 + n2)/2

if med < 5:
    print(f'Voce obteve a média de {med} e foi reprovado!')
elif med >= 7:
    print(f'Você obteve a média de {med} e foi aprovado!')
else:
    print(f'Voce está com a média de {med} e vai recorrer a recuperação!')

