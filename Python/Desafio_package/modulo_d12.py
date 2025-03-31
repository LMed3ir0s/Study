import copy

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

novos_produtos = copy.deepcopy(produtos)


def preco_aumentar(produtos_lista, percentual):
    porcentagem = 1 + (percentual/100)
    return [{**produto, 'preco': produto['preco'] * porcentagem} for produto in produtos_lista]
    
def imprimir_lista(list):
    for produto in list:
        print(f'Produto: {produto["nome"]}, Preço: R${produto["preco"]:.2f}')

def novo_produto(nome: str, preco: float):
    novo_item = {'nome': nome, 'preco': preco}
    novos_produtos.append(novo_item)

def ord_nome_decrescente(produtos_lista):
    return sorted(produtos_lista, key=lambda produto: produto['nome'], reverse=True)

def novo_produto_ord_nome(nome: str, preco: float):
    novo_item = {'nome': nome, 'preco': preco}
    novos_produtos.append(novo_item)
    return sorted(novos_produtos, key=lambda produto: produto['nome'])

#ajustar ordenacao novo_produto com antigo produtos

