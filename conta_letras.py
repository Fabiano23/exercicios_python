# Criar um programa que retorne a quantidade de cada letra dentro de uma frase

def conta_letras(frase):

    """>>> conta_letras('the sky is blue')
            {'t': 1, 'h': 1, 'e': 2, 's': 2, 'k': 1, 'y': 1, 'i': 1, 'b': 1, 'l': 1, 'u': 1}

            :param: frase
            :return: dicionário com a quantidade de cada letra dentro da frase passada como argumento"""

    dicionario_letras = {}
    frase = frase.replace(' ', '')
    for letra in frase:
        if letra not in dicionario_letras:
            dicionario_letras[letra] = frase.count(letra)
    return dicionario_letras

conta_letras('the sky is blue')
        


# Utilizando o método Counter() da biblioteca collections
from collections import Counter

def conta_letras2(frase):

    """>>> conta_letras('the sky is blue')
            Counter({'e': 2, 's': 2, 't': 1, 'h': 1, 'k': 1, 'y': 1, 'i': 1, 'b': 1, 'l': 1, 'u': 1})

            :param: frase
            :return: objeto Counter com a quantidade de cada letra na frase passada como argumento"""

    contagem = Counter(frase)
    del contagem[' ']
    return contagem

conta_letras2('the sky is blue')


