sexo = ''
continua = 'S'
idade = maioridade = qnt_homens = mulher_jovem = contagem = 0
teste = False

print('Cadastro de pessoas')
while continua == 'S':
    idade = int(input('Idade: '))
    sexo = 'x'
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper().[0]

    if idade > 17:
        maioridade += 1
    if sexo == 'M':
        qnt_homens += 1
    else:
        if idade < 20:
            mulher_jovem += 1

    continua = 'X'
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    contagem += 1

print('=-'*20)
print(f'''Nessas {contagem} Pessoas:
A) {maioridade} Tem mais de 18 anos.
B) {qnt_homens} São homens.
C) {mulher_jovem} mulheres tem menos de 20 anos.
''')
