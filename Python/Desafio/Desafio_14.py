 # Crie uma função zipper (como o zipper de roupas)
 # O trabalho dessa função será unir duas
 # listas na ordem.
 # Use todos os valores da menor lista.
 # Ex.:
 # ['Salvador', 'Ubatuba', 'Belo Horizonte']
 # ['BA', 'SP', 'MG', 'RJ']
 # Resultado
 # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list1, list2):
    intervalo = min(len(list1),len(list2))
    return [
        (list1[i], list2[i]) for i in range(intervalo)
    ]
    
lista_01 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_02 = ['BA', 'SP', 'MG', 'RJ']

print(list(zipper(lista_01, lista_02)))


####################################################################################################################

from itertools import zip_longest
 
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
