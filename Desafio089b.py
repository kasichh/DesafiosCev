lista = []
nome = apc_notas = str('')
nota1 = nota2 = 0

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))

    lista.append([nome, [nota1, nota2]])

    continua = str(input('Quer continuar? [S/N]'))

    if continua in 'Nn':
        break

print(f'{"No. "}{"Nome":<20}{"Média"}')
print("="*30)

for c, i in enumerate(lista):
    print(f'{c:<4}{i[0]:<20}{((i[1][0]+i[1][1])/2):>5}')
print("="*30)

while apc_notas != 999:
    apc_notas = int(input('Mostrar notas de qual aluno?(999 interrompe): '))

    print(f'Notas de {lista[apc_notas][0]} são {lista[apc_notas][1]}')
    print("="*30)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
