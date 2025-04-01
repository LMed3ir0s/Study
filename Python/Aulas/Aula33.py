"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    par = numero_int % 2 == 0
    par_text = 'impar'
    
    if par:
        print(f'O número digitado é par.')

    else:
        print(f'O número digitado é {par_text}.')


except:
        print(f'Você não digitou um número inteiro.')
    