#desafio 097
def escreva(mensagem):
    tamanho = len(mensagem)+4
    print('~' * tamanho)
    print(' ', mensagem, ' ')
    print('~' * tamanho)

escreva('pedro')
escreva('teste')
escreva('mensagem grande para propósitos de teste')
print('Sua vez')
texto = str(input('Digite um texto: '))
escreva(texto)
