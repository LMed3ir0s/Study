#Importlib e reload para recarregar modulo caso necessário, modulos são carregados apenas uma vez normalmente

import importlib
 
 import aula98_m
 
 print(aula98_m.variavel)
 
 for i in range(10):
     importlib.reload(aula98_m)
     print(i)
 
 print('Fim')