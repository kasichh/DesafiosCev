def notas(*notas, sit=False):
    """
    Programa para analisar situação de alunos
    :param notas: uma ou mais notas de alunos
    :param sit: Parametro opcional para apresentar situação
    :return: Lista de informações
    """
    dicionario = dict()

    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    media = sum(notas)/len(notas)
    dicionario['media'] = media
    if sit:
        if media>=7:
            situação = 'boa'
        elif media>=5:
            situação = 'meeh'
        else:
            situação = 'ruim'
        dicionario['situação'] = situação
    return dicionario


resp = notas(5.5, 5, 0, 6.5, sit=True)
print(resp)

