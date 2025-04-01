# => NOME

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')



# => SOMAR (Errado pois temos duas str) #

#numero_1 = input('Digite um número: ')
#numero_2 = input('Digite outro número: ')

#print(f'A soma dos números é: {numero_1 + numero_2}')



# => SOMAR (Errado pois convertendo a str em int na variable de "entrada do usuário", caso ele digite algo diferente de um int o programa da um erro sem possibilidade de checagem#

# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))

# print(f'A soma dos números é: {numero_1 + numero_2}')

# => SOMAR DOIS NUMEROS DE FORMA CORRETA

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')