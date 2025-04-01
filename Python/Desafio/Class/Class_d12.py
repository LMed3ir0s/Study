class D_12:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @staticmethod
    def novo_produto_ord_nome(self, lista: list, nome: str, preco: float):
        novo_item = {'nome': nome, 'preco': preco}
        lista.append(novo_item)        
        return sorted(lista, key=lambda produto: produto['nome'])
    
novos_produtos = []
teste = D_12.novo_produto_ord_nome(novos_produtos,"Produto Novo 03", 50.50)

print(novos_produtos)


class D_12:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
    
    @staticmethod
    def novo_produto_ord_nome(lista: list, nome: str, preco: float):
        novo_item = {'nome': nome, 'preco': preco}
        lista.append(novo_item)
        return sorted(lista, key=lambda produto: produto['nome'])
    
def main():
    novos_produtos = []
    novos_produtos = D_12.novo_produto_ord_nome(novos_produtos, "Produto novo 03", 50.50)

    print(novos_produtos)

if __name__ == "__main__":
    main()
