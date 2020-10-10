# Utilizando o fatiamento de string
def reverter_palavras(frase):

    """>>> reverter_palavras('the sky is blue')
        'blue is sky the'

        :param: frase
        :return: frase com as palavras invertidas"""

    palavras_separadas = frase.split(' ')
    return ' '.join(palavras_separadas[::-1])
    

reverter_palavras('the sky is blue')


# Utilizando o método reverse()

def reverter_palavras2(frase):
    palavras_separadas = frase.split(' ')
    palavras_separadas.reverse()
    return ' '.join(palavras_separadas)

reverter_palavras2('the sky is blue')
