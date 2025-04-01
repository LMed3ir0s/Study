"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Que horas são? Digite apenas número inteiro: ')

try:

    hora_int = int(entrada)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')

    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')

    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')

    else:
        print('Você não digitou uma hora válida')

except:
    print('Você digitou algo diferente de um horário')
