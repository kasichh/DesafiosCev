nome = input('Fala o nome ae corno: ').strip()

nome = nome.title()

teste = 'Silva' in nome

print(f'Tem "Silva" em {nome}?')
print(teste)