from abc import ABC, abstractmethod

class D_13base(ABC):
    @abstractmethod
    def parametros(self, x, y):
        pass

class somar(D_13base):
    def parametros(self, x,y):
        return x + y

class multiplicar(D_13base):
    def parametros(self, x,y):
        return x * y





        
