import datetime

ano = int(str(datetime.date.today())[:4])
nasc = int(input('Digite o ano do seu nascimento: '))
idade = ano - nasc

print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Atleta \033[35mMIRIM\033[m')
elif idade <= 14:
    print('Atleta \033[36mINFANTIL\033[m')
elif idade <= 19:
    print('Atleta \033[32mJUNIOR\033[m')
elif idade <= 25:
    print('Atleta \033[35mSENIOR\033[m')
else:
    print('Atleta \033[31mMASTER\033[m')
