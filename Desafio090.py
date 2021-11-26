aluno = dict()

aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = int(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

print('Informações do aluno:')
for k, v in aluno.items():
    print(f'{k} = {v}')