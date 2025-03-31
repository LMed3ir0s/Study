"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# dig_1 = input("Digite o primeiro numero do CPF: ")
# dig_2 = input("Digite o segundo numero do CPF: ")
# dig_3 = input("Digite o terceiro numero do CPF: ")
# dig_4 = input("Digite o quarto numero do CPF: ")
# dig_5 = input("Digite o quinto numero do CPF: ")
# dig_6 = input("Digite o sexto numero do CPF: ")
# dig_7 = input("Digite o setimo numero do CPF: ")
# dig_8 = input("Digite o oitavo numero do CPF: ")
# dig_9 = input("Digite o nono numero do CPF: ")
# CPF = dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 + dig_7 + dig_8 + dig_9
# CPF_1 = dig_1 + dig_2 + dig_3
# CPF_2 = dig_4 + dig_5 + dig_6
# CPF_3 = dig_7 + dig_8 + dig_9
CPF = '746824890'
nove_dig = CPF[:9]
resultado_1 = 0
resultado_2 = 0
primeiro_dig = 0
segundo_dig = 0
regressao_1 = 10
regressao_2 = 11


# print('CPF: ', CPF_1, '.', CPF_2, '.', CPF_3)


for i in nove_dig:
    resultado_1 += (int(i) * regressao_1)
    regressao_1 -= 1

    verif_dig1 = 0
    verif_dig1 = (resultado_1 * 10) % 11
    
    if verif_dig1 > 9:
        primeiro_dig = 0    
    else:
        primeiro_dig = verif_dig1

    
    dez_dig = CPF + str(primeiro_dig)
for i in dez_dig:
    resultado_2 += (int(i) * regressao_2)
    regressao_2 -= 1

    verif_dig2 = 0
    verif_dig2 = (resultado_2 * 10) % 11

    if verif_dig2 > 9:
        segundo_dig = 0
    else:
        segundo_dig = verif_dig2

print(primeiro_dig, segundo_dig)