from sys import path
 # from sys import path
 
import Aulas_package.modulo
from Aulas_package import modulo
from Aulas_package.modulo import *
 # import Aulas_package.modulo
 # from Aulas_package import modulo
 # from Aulas_package.modulo import *
 
 # from Aulas_package.modulo import soma_do_modulo
 # # from Aulas_package.modulo import soma_do_modulo
 
 # print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(Aulas_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
 # # print(*path, sep='\n')
 # print(soma_do_modulo(1, 2))
 # print(Aulas_package.modulo.soma_do_modulo(1, 2))
 # print(modulo.soma_do_modulo(1, 2))
 # print(variavel)
 # print(nova_variavel)
from Aulas_package.modulo import fala_oi, soma_do_modulo
 
print(__name__)
fala_oi()