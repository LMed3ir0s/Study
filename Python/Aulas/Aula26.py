"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'LUCAS'

print (
    f'{variavel}'
    )


print (
    f'{variavel: >10}'
    )



print (
    f'{variavel: <10}.'
    )



print (
    f'{variavel:x^10}.'
    )