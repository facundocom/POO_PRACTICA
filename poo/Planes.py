import abc
from abc import ABC
class Plan:
    __nombrecomp: str
    __duracion: int
    __cobertura: str
    __precio: float
    
    def __init__(self, nombrecomp, duracion, cobertura, precio):
        self.__nombrecomp=nombrecomp
        self.__duracion=duracion
        self.__cobertura=cobertura
        self.__precio=precio

    def __str__(self):
        return f"Nombre:{self.__nombrecomp}, Duración: {self.__duracion}, Cobertura: {self.__cobertura}, Precio: {self.__precio}"
    
    def getNom(self):
        return self.__nombrecomp
    
    def getDur(self):
        return self.__duracion
    
    def getCob(self):
        return self.__cobertura.lower()
    
    def getPre(self):
        return self.__precio
    
    @abc.abstractmethod
    def descuentos(self):
        pass

    def importefinal(self):
        return self.__precio + self.descuentos()

    def mostrarDatos(self):
        print ('\n-----Datos de la compañía-----\n')
        print (f'Nombre de la compañía: {self.__nombrecomp}\n')
        print (f'Duración en días del plan: {self.__duracion}\n')
        print (f'Cobertura geográfica del plan: {self.__cobertura}\n')
        print (f'Precio base del plan: {self.__precio}\n')
        print (f'Precio con descuentos: {self.importefinal()}\n')
        

    
