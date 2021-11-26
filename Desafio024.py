cidade = input('Digite o nome da cidade: ')

cidade = cidade.title()

print(f'Começa com "Santo" em {cidade.strip()}?')

dividido = cidade.split()
teste = 'Santo' in dividido[0]
print(teste)
