"""
Enunciado do exercício:
https://www.programcreek.com/2015/03/rotate-array-in-java/

Métodos a serem memorizados:

Lista:

    >>> list('banana')      # string para lista
    ... ['b', 'a', 'n', 'a', 'n', 'a']

    >>> lst = [1, 2]    # cópia de lista
    >>> copia = list(lst)
    >>> copia
    ... [1, 2]
    >>> copia is lst    # Não é o mesmo objeto, novo espaço alocado na memória pra guardar a cópia da lista
    ... False
 
String:

    >>> ''.join(['b', 'a', 'n', 'a', 'n', 'a'])    # lista para string
    ... banana
    >>> '-'.join(['b', 'a', 'n', 'a', 'n', 'a'])
    ... b-a-n-a-n-a

    >>> str('banana')    # Cópia de string
    ... 'banana'

Métodos em comum (string e lista):

    >>> s =  'banana'
    >>> lst = ['b', 'a', 'n', 'a', 'n', 'a']
    
    >>> s[0], lst[0]  # indices
    ... b b

    >>> len(s), len(lst)     # tamanho
    ... 6 6

    >>> s[2:5], lst[2:5]     # slice
    ... nan ['n', 'a', 'n']
    >>> s[4:], lst[4:]     
    ... na ['n', 'a']
    >>> s[-1], lst[-1]     
    ... a a

    >>> sorted(s), sorted(lst)    # ordenação
    ... ['a', 'a', 'a', 'b', 'n', 'n'] ['a', 'a', 'a', 'b', 'n', 'n']   # transforma string s em uma lista
    >>> lst 
    ... ['b', 'a', 'n', 'a', 'n', 'a']    #lst continua ordenado, o sorted() faz uma cópia da lista original
    
    >>> lst.sort()    # método da própria lista, altera a lista original
    >>> lst
    ... ['a', 'a', 'a', 'b', 'n', 'n']
"""


from typing import List

def rotaciona_array(lista: list, k: int):
    """
    >>> lista = [1, 2, 3, 4, 5, 6, 7]
    >>> list(rotaciona_array(lista, 3))
    ... [5, 6, 7, 1, 2, 3, 4]
    >>> for elemento in rotaciona_array(lista, 1):
    ...     print(elemento)
    ...
    7
    1
    2
    3
    4
    5
    6
    >>> next(iter(rotaciona_array(lista, 2)))    # retorna primeira elemento da lista retornada
    ... 6
    
    :param iteravel:
    :param k:
    :return: 
    """
    
    primeira_fatia = lista[-k : ]
    segunda_fatia = lista[ : -k]
    return primeira_fatia + segunda_fatia


# Função mais performática, pois acessa os elementos através dos índices em que se encontram na lista original

from itertools import chain

def rotacionar_generator(lista: list, k: int):
    """
    >>> lista = [1, 2, 3, 4, 5, 6, 7]
    >>> list(rotaciona_generator(lista, 3))
    ... [5, 6, 7, 1, 2, 3, 4]
    >>> for elemento in rotaciona_generator(lista, 1):
    ...     print(elemento)
    ...
    7
    1
    2
    3
    4
    5
    6
    >>> next(iter(rotacionar_generator(lista, 2)))    # retorna primeira elemento da lista retornada
    ... 6
    
    :param iteravel:
    :param k:
    :return: 
    """
    
    n = len(lista)
    primeira_fatia_indices = range(n - k, n)
    segunda_fatia_indices = range(n - k)
    indices_rotacionados = chain(primeira_fatia_indices, segunda_fatia_indices)

    for indices_rotacionado in indices_rotacionados:
        yield lista[indices_rotacionado]


#Comparando performance das duas funções 

from time import time

if __name__ == '__main__':
    for tamanho in range(1000, 100000, 1000):
        lista = list(range(tamanho))
        inicio = time()
        elemento = next(iter(rotaciona_array(lista, 1)))
        final = time()
        print(f'(Rotacionar) Tamanho {tamanho}: {elemento}, {final - inicio}')

        inicio = time()
        elemento = next(rotacionar_generator(lista, 1))
        final = time()
        print(f'(Rotacionar Geradora) Tamanho {tamanho}: {elemento}, {final - inicio}')