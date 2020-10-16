def conta_letras(s: str):

    """
    >>> conta_letras('fabiano')
            {'f': 1, 'a': 2, 'b': 1, 'i': 1, 'n': 1, 'o': 1}
    >>> conta_letras('Ffabiano')
            {'F': 1, 'f': ', 'a': 2, 'b': 1, 'i': 1, 'n': 1, 'o': 1}
    >>> conta_letras('banana')
            {'b': 1, 'a': 3, 'n': 2 }
            :param s: 
            :return:
            """

    dicionario_letras = {}     # {}

    for letra in s:    # s = 'fabiano'  letra = 'f',    letra = 'a', ..., letra = 'o'
        if letra not in dicionario_letras:
            dicionario_letras[letra] = s.count(letra)  # {'f' : 1},    {'f' : 1, 'a' : 2}, ...,   {'f': 1, 'a': 2, 'b': 1, 'i': 1, 'n': 1, 'o': 1}

    return dicionario_letras



# Utilizando o método Counter() da biblioteca collections

from collections import Counter

def conta_letras2(s: str):

    """
    >>> conta_letras('fabiano')
            {'f': 1, 'a': 2, 'b': 1, 'i': 1, 'n': 1, 'o': 1}
    >>> conta_letras('Ffabiano')
            {'F': 1, 'f': ', 'a': 2, 'b': 1, 'i': 1, 'n': 1, 'o': 1}
    >>> conta_letras('banana')
            {'b': 1, 'a': 3, 'n': 2 }
            :param s: 
            :return:
            """

    return dict(Counter(s))    # {'b': 1, 'a': 3, 'n': 2 }
