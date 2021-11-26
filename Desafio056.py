nome = str('')
idade = 0
sexo_teste = bool(False)
soma_idade = 0
mulhermenor = 0
sexo_testef = bool(False)
homemvelho = 0
maisvelho = str()

for c in range(0,4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [m/f]: ').lower()
    soma_idade += idade
    if sexo == 'm' and idade > homemvelho:
        homemvelho = idade
        maisvelho = nome
        sexo_teste = True
    else:
        sexo_testef = True
        if idade < 20:
            mulhermenor += 1
print('=-'*20)
print(f'A média de idade é: {soma_idade/4}')

if sexo_teste == True:
    print(f'O homem mais velho é o {maisvelho} e tem {homemvelho} anos')
else:
    print('Nenhum homem foi registrado')

if sexo_testef == True:
    if mulhermenor >= 1:
        print(f'A quantidade de mulheres mais novas do que 20 anos é: {mulhermenor}')
    else:
        print('Nenhuma mulher registrada tem menos de 20 anos!')
else:
    print('Nenhuma mulher foi registrada')

