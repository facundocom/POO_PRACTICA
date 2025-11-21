##Vidable Agustin
# E009-70 LSI
# 44317140

class Movilidad:
    __patente:str
    __tipo:str
    __capacidad:int
    __impPatente:float
    __marca:str
    __modelo:str

    def __init__(self, patente, tipo, capacidad, importe, marca, modelo):
        self.__patente = patente
        self.__tipo = tipo
        self.__capacidad = capacidad
        self.__importe = importe
        self.__marca = marca
        self.__modelo = modelo
        self.__fecha = None

    def __str__(self):
        return f"Patente: {self.__patente}, Tipo: {self.__tipo}, Capacidad: {self.__capacidad}, Impuesto Patente: {self.__impPatente}, Marca: {self.__marca}, Modelo: {self.__modelo}"

    def getPatente(self):
        return self.__patente

    def getTipo(self):
        return self.__tipo
    
    def setFecha(self, fecha):
        self.__fecha = fecha

    def getCapacidad(self):
        return self.__capacidad

    def getImpPatente(self):
        return self.__impPatente

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    
    def getFecha(Self):
        return None
    
    def __lt__(self, other):
        return self.__patente < other.__patente





