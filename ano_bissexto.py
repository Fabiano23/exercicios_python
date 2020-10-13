# Função que recebe um ano como argumento e retorna se ele é/foi ou não bissexto.


# Pegando o ano atual da máquina local com o método data da biblioteca datetime
# O objetivo é ajustar  frase da função de acordo com o ano no momento de sua execução
from datetime import date
ano_atual = date.today().year




def ano_bissexto(ano):

    """>>> ano_bissexto(1988)
        O ano 1988 foi bissexto!

        :param: ano
        :return: frase dizendo se o ano passado como argumento é ou não um ano bissexto"""

    if (ano % 4 == 0 and ano % 100 != 0 and ano <= ano_atual) or (ano % 400 == 0 and ano <= ano_atual):
        return f'O ano {ano} foi bissexto!'
    elif (ano % 4 == 0 and ano % 100 != 0 and ano > ano_atual) or (ano % 400 == 0 and ano > ano_atual):
        return f'O ano {ano} será bissexto!'
    elif (ano % 4 != 0 and ano % 100 == 0 and ano <= ano_atual) or (ano % 400 != 0 and ano <= ano_atual):
        return f'{ano} não foi um ano bissexto...'
    else:
        return f'{ano} não será um ano bissexto...'



# Lista com anos bissextos
anos_bissextos = [1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020,
                  2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052]

# Testando função com cada ano da lista de anos bissextos
for ano in anos_bissextos:
    print(ano_bissexto(ano))



# Lista com anos não bissextos
anos_nao_bissextos = [1900, 1950,  2002, 2030, 2037, 2100]

# Testando função com cada valor da lista de anos não bissextos
for ano in anos_nao_bissextos:
    print(ano_bissexto(ano))
