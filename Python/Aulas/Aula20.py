"""
##################################################################
         => EXERCICIO PRIMEIRO OU SEGUNDO VALOR MAIOR <=         
##################################################################
"""



"""
TESTE 1)
"""

# entrada_1 = input('Digite um valor:')
# entrada_2 = input('Digite outro valor:')

# int_entrada_1 = int(entrada_1)
# int_entrada_2 = int(entrada_2)

# condicao1 = int_entrada_1 == int_entrada_2
# condicao2 = int_entrada_1 > int_entrada_2
# condicao3 = int_entrada_1 < int_entrada_2
# condicao4 = entrada_1 != int


# if condicao1:
#     print('O primeiro valor é igual ao segundo valor.')

# elif condicao2:
#     print('O primeiro valor é maior que o segundo valor.')

# elif condicao3:
#     print('O primeiro valor é menor que o segundo valor.')

# elif condicao4:
#     print('Você não digitou um valor válido.')

# else:
#     print('Você não digitou um valor válido.')



################################################################


"""
TESTE 2)
"""

# entrada_1 = input('Digite um valor:')
# entrada_2 = input('Digite outro valor:')


# condicao1 = entrada_1 == entrada_2
# condicao2 = entrada_1 > entrada_2
# condicao3 = entrada_1 < entrada_2


# if condicao1:
#     print('O primeiro valor é igual ao segundo valor.')

# elif condicao2:
#     print('O primeiro valor é maior que o segundo valor.')

# elif condicao3:
#     print('O primeiro valor é menor que o segundo valor.')

# else:
#     print('Você não digitou um valor válido.')



################################################################


"""
TESTE 3)
"""

entrada_1 = input('Digite um valor:')
entrada_2 = input('Digite outro valor:')


condicao1 = entrada_1 == entrada_2
condicao2 = entrada_1 > entrada_2



if condicao1:
    print(
        f'O primeiro valor = {entrada_1} é igual ao segundo valor, que também é {entrada_2}.'
        )

elif condicao2:
    print(
        f'O primeiro valor = {entrada_1}, é maior'
        f' que o segundo valor = {entrada_2}.'
        )

else:
    print(
        f'O primeiro valor = {entrada_1}, é menor'
        f' que o segundo valor = {entrada_2}.'
        )