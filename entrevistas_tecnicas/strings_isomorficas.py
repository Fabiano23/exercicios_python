"""
Enunciado: https://www.programcreek.com/2014/05/leetcode-isomorphic-strings-java/
"""

def verifica_se_sao_isomorficas(s: str, t: str):
    """
    >>> verifica_se_sao_isomorficas('egg', 'foo')
    True
    >>> verifica_se_sao_isomorficas('egg', 'foe')
    False
    >>> verifica_se_sao_isomorficas('egg', 'ooo')
    True
    >>> verifica_se_sao_isomorficas('egg', 'fooo')
    False
    >>> verifica_se_sao_isomorficas('egge', 'foo')
    False
    
    :param s:
    :param t:
    :return: boleano informando se s e t são (True) ou não (False) isomórficas
    """

    if len(s) != len(t):
        return False
    
    dicionario = {}

    for letra_de_s, letra_de_t in zip(s, t):
        try:
            valor_de_s_eh_respectivo_a_letra_de_t = (dicionario[letra_de_s] == letra_de_t)
        except KeyError:
            dicionario[letra_de_s] = letra_de_t
        else:
            if not valor_de_s_eh_respectivo_a_letra_de_t:
                return False
            
    return True

