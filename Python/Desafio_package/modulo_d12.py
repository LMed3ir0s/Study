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

def ord_nome_crescente(produtos_lista):
    return sorted(produtos_lista, key=lambda produto: produto['nome'])

def ord_preco_crescente(produtos_lista):
    return sorted(produtos_lista, key=lambda produto: produto['preco'])

def novo_produto_ord_nome(novo_produto,ord_preco_crescente):
    novo_produto()
    ord_preco_crescente()
    return

#ajustar ordenacao novo_produto com antigo produtos



2. @abstractmethod (do módulo abc)
Indica que um método deve ser implementado obrigatoriamente em classes filhas.

Usado em classes abstratas.

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass  # Implementação obrigatória nas subclasses

class Quadrado(Forma):
    def calcular_area(self):
        return "Área calculada!"
------------------------------------------------------------------
3. @dataclass (do módulo dataclasses)
Facilita a criação de classes para armazenar dados, gerando automaticamente métodos como __init__ e __repr__.

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

p = Pessoa(nome="Ana", idade=25)
print(p)  # Saída: Pessoa(nome='Ana', idade=25)
------------------------------------------------------------------
4. @staticmethod e @classmethod (Já explicado no post acima)
