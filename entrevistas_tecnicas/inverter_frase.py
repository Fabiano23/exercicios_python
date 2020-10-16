# Utilizando o fatiamento de string
def reverter_palavras(frase: str):

    """
    >>> reverter_palavras('the sky is blue')
        'blue is sky the'

        :param frase: 
        :return:
        """

    palavras_separadas = frase.split(' ')    # ['the', 'sky', 'is', 'blue']

    return ' '.join(palavras_separadas[::-1])    # 'blue is the sky'
    


# Utilizando o método reverse()

def reverter_palavras2(frase: str):

    """
    >>> reverter_palavras('the sky is blue')
        'blue is sky the'

        :param frase: 
        :return:
        """

    palavras_separadas = frase.split(' ')    # ['the', 'sky', 'is', 'blue']

    palavras_separadas.reverse()    # ['blue', 'is', 'the', 'sky']

    return ' '.join(palavras_separadas) # 'blue is the sky'

