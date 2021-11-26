frase = input('Digite uma frase: ').strip()
cont_a = frase.lower().count('a')
procura = frase.lower().find('a')
procure = frase.lower().rfind('a')

print(f'Para a frase {frase.title()}, a letra "A" aparece: {cont_a} vezes!')
print(f'A letra "A" aparece pela primeira vez em na {procura + 1} posicao')
print(f'A letra "A" aparece pela ultima vez em na {procure + 1} posicao')
