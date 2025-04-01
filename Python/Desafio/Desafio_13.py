from Class.Class_d13 import somar, multiplicar, D_13base

# Adiando execução de funções #

def criar_funcao(operacao: D_13base, x):
    def interna(y):
        return operacao.parametros(x, y)
    return interna


soma_com_cinco = criar_funcao(somar(), 5)
multiplica_por_dez = criar_funcao(multiplicar(), 10)

print(f'A soma dos numeros é: {soma_com_cinco(10)}')
print(multiplica_por_dez(10))

