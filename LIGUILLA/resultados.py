class Resultado:
    __fecha:str
    __idLocal:str
    __golLocal:int
    __idVis:int
    __golVis:int
    __precio=45000

    def __init__(self,fecha,idL,golL,idV,golV):
        self.__fecha=fecha
        self.__idLocal=idL
        self.__golLocal=golL
        self.__idVis=idV
        self.__golVis=golV

    @classmethod
    def precio(cls):
        return cls.__precio
        
    def getFecha(self):
        return self.__fecha
    def getIdLocal(self):
        return self.__idLocal
    def getIdVis(self):
        return self.__idVis
    def mostrar(self,local,visitante):
        print(f"{local}:{self.__golLocal}-{self.__golVis}:{visitante} ")
    def getGolLocal(self):
        return self.__golLocal
    def getGolVis(self):
        return self.__golVis