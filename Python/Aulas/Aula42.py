'''
Exercicio 01
'''

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'



# i = 0
# qtd_letra_apareceu = 0
# qtd_apareceu_mais_x = 0
# letra_apareceu_mais_x = ''



# while i < len(frase):
#     letra_atual = frase[i]
#     qtd_letra_apareceu = frase.count(letra_atual)

#     print(f'{letra_atual}, {qtd_letra_apareceu}.')
#     i += 1



i = 0
qtd_apareceu_mais_x = 0
letra_apareceu_mais_x = ''



while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_x < qtd_letra_apareceu_atual:
        qtd_apareceu_mais_x = qtd_letra_apareceu_atual
        letra_apareceu_mais_x = letra_atual

    i += 1

print(
    f'A letra que repetiu mais vezes foi a "{letra_apareceu_mais_x}", no total de {qtd_apareceu_mais_x} vezes. '
)