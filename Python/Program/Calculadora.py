"""
Calculadora ultilzando While
"""

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador +, -, /, ou *: ')

    numeros_validos = None
    operadores_validos = '+-/*'
    num_1_float = 0
    num_2_float = 0


    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    #     operador = str(operador)    

    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Um ou ambos dos números não são válidos.')
        continue

    if operador not in operadores_validos:
        print('Você digitou um operador inválido.')
        continue

    if len(operador) > 1:
        print('Você digitou mais de um operador.')
        continue

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'O resultado da soma dos números {numero_1} e {numero_2} é {soma:.2f} ')

    if operador == '-':
        subtracao = num_1_float - num_2_float
        print(f'O resultado da subtração dos números {numero_1} e {numero_2} é {subtracao:.2f} ')

    if operador == '/':
        divisao = num_1_float / num_2_float
        print(f'O resultado da divisão dos números {numero_1} e {numero_2} é {divisao:.2f} ')

    if operador == '*':
        multiplicacao = num_1_float * num_2_float
        print(f'O resultado da multiplicação dos números {numero_1} e {numero_2} é {multiplicacao:.2f} ')


###
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break