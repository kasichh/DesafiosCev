peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
print(f'imc seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('obesidade')
else:
    print('Obesidade mórbida')
