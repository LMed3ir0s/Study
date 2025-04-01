
# """
# Iterando strings com while
# """
# #       012345678910111213
# nome = 'Lucas Medeiros'  # Iteráveis
# #      1413121110987654321


entrada = input('Entre com um nome: ')
nome = str(entrada)
tamanho_nome = len(nome)
indice = 0
novo_nome = ''

while indice < len(nome):
    print(nome[indice])
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    # novo_nome += letra'
    # novo_nome += '*'

print(novo_nome)   
