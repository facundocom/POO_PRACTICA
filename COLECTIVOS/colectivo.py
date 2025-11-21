
class Colectivo:
    __patente:str
    __marca:str
    __modelo:str
    __capacidad:int
    __dni:int
    __consumo=35

    def __init__(self,pat,mar,mod,cap,dni):
        self.__patente=pat
        self.__marca=mar
        self.__modelo=mod
        self.__capacidad=cap
        self.__dni=dni
    
    def getDocumento(self):
        return self.__dni
    def getPatente(self):
        return self.__patente
    
    @classmethod
    def getConsumo(cls):
        return cls.__consumo
    