"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
             is_int(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


def is_int(param):
    if not isinstance(param, int):
        raise TypeError('param deve ser um int')

@criar_funcao
def soma(a, b):
    return a + b

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        soma(lista1[i],lista2[i]) for i in range(intervalo)
    ]


####################################################################################################################

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print(list(zipper(lista_a, lista_b)))

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)


####################################################################################################################

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


####################################################################################################################

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)