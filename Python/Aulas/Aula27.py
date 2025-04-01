"""
Fatiamento de strings

 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""


variavel = 'Olá mundo'

print(variavel[4:]) #iniciando do indice 4 ate o fim "" significa ate o fim ou a partir do inicio

print(variavel[:5]) #do inicio até o indice "5"
 
print(variavel[2:7]) #do indice "2" ate o "7"

print(variavel[-9:-1]) # "

print(variavel[-1:-9]) # "

print(len(variavel)) #qts caracters na variavel

print(len(variavel[3])) # qts caracters no indice

print(variavel[0:9:3]) #passo "3" pulando caracter pode ser de "n" em "n"




print(variavel[::-1]) #passo negativo, inverte a string