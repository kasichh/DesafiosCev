palavras = ('texto', 'palavras', 'objeto', 'osbervacao', 'programacao', 'teste', 'mineracao')

for c in palavras:
    print(f'A palavra {c.upper()} contém as vogais: ', end='')

    palavra = c.lower()

    for d in palavra:
        if d in 'aeiou':
            print(d, end=' ')
    print('')

