"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


import os

palavra_secreta = 'lucas'
letras_acertadas = ''
tentativa = 0

while True:
    
    entrada = input('Digite uma letra: ')
    tentativa += 1

    if len(entrada) > 1:
        print('Por favor digite apenas uma letra.')    
        continue

    if entrada not in palavra_secreta:        
        print('Você digitou uma letra incorreta.')        
        continue

    if entrada in palavra_secreta:
        letras_acertadas += entrada
        
        palavra_formada = ''        
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta    
        else:
            palavra_formada+= '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Parábens você acertou a Palavra Secreta "{palavra_secreta}", foram no total {tentativa} tentativas."')
        letras_acertadas = ''
        tentativa = 0

        sair = input('Deseja sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break
    