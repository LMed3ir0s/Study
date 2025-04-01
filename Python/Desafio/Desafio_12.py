import copy

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]
 
def imprimir_lista(list):
    for produto in list:
        print(f"Produto: {produto['nome']}, Preço: R$ {produto['preco']:.2f}")
    return

# 1)Aumente os preços dos produtos a seguir em 10%
produtos_aumento10 = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos
]

# 2)Gere novos_produtos por deep copy (cópia profunda)
# copy, sorted, produtos.sort
novos_produtos = copy.deepcopy(produtos)
def novo_produto(nome: str, preco: float):
    novo_item = {'nome': nome, 'preco': preco}
    novos_produtos.append(novo_item)
    return
novo_produto('Produto 6', 300.20)

# 3)Ordene os produtos por nome decrescente (do maior para menor)
def ordernar_nomedecrescente(list):
    return sorted(list, key= lambda produto: produto['nome'], reverse=True )

# 4)Gere produtos_ordenados_por_nome por deep copy (cópia profunda) 
def ordernar_nomecrescente(list):
    return sorted(list, key= lambda produto: produto['nome'])

# 5)Ordene os produtos por preco crescente (do menor para maior)
def ordernar_precocrescente(list):
    return sorted(list, key= lambda produto: produto['preco'])

# 6)Gere produtos_orreco denados_por_ppor deep copy (cópia profunda)
n_prod_ord_preco = copy.deepcopy(produtos)
def novo_produto_ordenado_preco(nome: str, preco: float):    
    novo_item = {'nome': nome, 'preco': preco}
    n_prod_ord_preco.append(novo_item)
    return ordernar_precocrescente(n_prod_ord_preco)

novo_produto_ordenado_preco("Produto 7", 777.33)

#1)
# imprimir_lista(produtos_aumento10)
# print()

#2)
# imprimir_lista(novos_produtos)
# print()

#3)
# nomeprodutos_decrescente = ordernar_nomedecrescente(produtos)
# print(*nome, sep='\n')
# print()

#4)
# nomeprodutos_crescente = ordernar_nomecrescente(produtos)
# print(*nomeprodutos_crescente, sep='\n')
# print()

#5)
# precoprodutos_crescente = ordernar_precocrescente(produtos)
# print(*precoprodutos_crescente, sep='\n')
# print()

#6)
# imprimir_lista(n_prod_ord_preco)
# print()

