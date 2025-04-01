from abc import ABC, abstractmethod

# Classe abstrata
class OperacaoBase(ABC):
    @abstractmethod
    def executar(self, x, y):
        pass


class SomaOperacao(OperacaoBase):
    def executar(self, x, y):
        return x + y


class MultiplicaOperacao(OperacaoBase):
    def executar(self, x, y):
        return x * y


# Função para criar uma função baseada na operação
def criar_funcao(operacao: OperacaoBase, x):
    def interna(y):
        return operacao.executar(x, y)
    return interna


# Utilizando as operações
soma_com_cinco = criar_funcao(SomaOperacao(), 5)
multiplica_por_dez = criar_funcao(MultiplicaOperacao(), 10)

print(soma_com_cinco(10))  # Saída: 15
print(multiplica_por_dez(10))  # Saída: 100