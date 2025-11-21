class Colectivo:
    __patente: str
    __marca: str
    __modelo: str
    __capacidad: int
    __dniConductor: int
    __consumoPromedio = 35

    def __init__(self, patente, marca, modelo, capacidad, dni):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__dniConductor = dni

    def getPatente(self):
        return self.__patente
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getCapacidad(self):
        return self.__capacidad
    
    def getDni(self):
        return self.__dniConductor
    
    @classmethod
    def getConsumoPromedio(cls):
        return cls.__consumoPromedio
    
