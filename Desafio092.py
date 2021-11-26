pessoa = dict()
from datetime import datetime

data = datetime.now().year

pessoa['nome'] = str(input('Digite o nome: '))
ano_nascimento = int(input('Digite a data de nasciemento: '))
pessoa['idade'] = data - ano_nascimento
pessoa['CTPS'] = int(input('Digite a CTPS. 0 Para nulo: '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Digite o salário: '))
    aposentadoria = pessoa['contratação'] + 35
    pessoa['aposentadoria'] = aposentadoria - ano_nascimento

print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')