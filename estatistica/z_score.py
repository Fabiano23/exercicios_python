import numpy as np

"""
Conceito: Z score é uma medida estatística que calcula quantos 
desvios padrão um determinado dado está afastado da media da distribuição a qual pertence.

https://www.investopedia.com/terms/z/zscore.asp#:~:text=A%20Z%2Dscore%20is%20a,identical%20to%20the%20mean%20score.
"""

def z_score(distribuicao):
    
    """
    >>> distribuicao = [1, 3, 5, 7]
    >>> z_score(distribuicao)
    [-1.3416407864998738, -0.4472135954999579, 0.4472135954999579, 1.3416407864998738]
  
    :param distribuição: sequência python com qualquer distribuição de dados de tipo quantitativo discreto ou contínuo
    :return: uma lista com os z scores da distribuição
    """
  
    media = np.mean(distribuicao) #Media da distribuição
  
    desvio_padrao = np.std(distribuicao) #Desvio padrão da distribuição
  
    # Calculando o z_scores de cada valor da distribuição com list comprehension
    z_scores = [(x - media) / desvio_padrao for x in distribuicao]
  
    return z_scores # lista com os z_scores calculados