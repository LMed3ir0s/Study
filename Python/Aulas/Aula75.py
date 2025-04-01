# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

numero = input('Digite um numero: ')
int_numero = int(numero)

# def duplicar(numero):
#     return numero * 2
  
# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f'O dobro do numero {numero}, e', duplicar(int_numero))
print(f'O Triplo do numero {numero}, e', triplicar(int_numero))
print(f'O Quadruplo do numero {numero}, e', quadruplicar(int_numero))

