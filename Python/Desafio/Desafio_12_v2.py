import sys
import os
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Desafio_package import (
    produtos, preco_aumentar, imprimir_lista, novo_produto, novos_produtos, ord_nome_decrescente,
    novo_produto_ord_nome, novos_produtos
    )




print("Produtos Inicial")
imprimir_lista(produtos)
print()

# 1)Aumente os preços dos produtos a seguir em 10%
print("# 1)Aumente os preços dos produtos a seguir em 10%")
novo_preco = preco_aumentar(produtos, 10)
imprimir_lista(novo_preco)
print()

# 2)Gere novos_produtos por deep copy
print("# 2)Gere novos_produtos por deep copy")
novo_produto('PRODUTO NOVO 01', 33.33)
imprimir_lista(novos_produtos)
print()

# 3)Ordene os produtos por nome decrescente
print("# 3)Ordene os produtos por nome decrescente")
imprimir_lista(ord_nome_decrescente(novos_produtos))
print()

# 4)Gere produtos_ordenados_por_nome por deep copy
print("# 4)Gere produtos_ordenados_por_nome por deep copy")
novo_produto_ord_nome('PRODUTO NOVO 02', 77.77)
imprimir_lista(novos_produtos)
print()

# # 5)Ordene os produtos por preco crescente
# print("# 5)Ordene os produtos por preco crescente")
# imprimir_lista()
# print()

# # 6)Gere produtos_ordenados_por_preco por deep copy
# print("# 6)Gere produtos_ordenados_por_preco por deep copy")
# imprimir_lista()
# print()

# ##implementar escolhas/saida e limpar /// Multiplos produtos

