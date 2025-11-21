
class Gamerr():
    __id:int
    __dni:int
    __nombre:str
    __apellido:str
    __alias:str
    __plan:str
    __importe:int
    __limite:int
    
    def __init__(self,id,dni,nom,ap,al,plan,imp,lim):
        self.__id=id
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ap
        self.__alias=al
        self.__plan=plan
        self.__importe=imp
        self.__limite=lim
    
    def getID(self):
        return self.__id
    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getAlias(self):
        return self.__alias
    def getPlan(self):
        return self.__plan
    def getImporte(self):
        return self.__importe
    def getLimite(self):
        return self.__limite
    def mostrar(self):
        print(f"Dni{self.__dni},Apellido: {self.__apellido}")
        print(f"Alias:{self.__alias},Plan: {self.__plan} Importe:{self.__importe}")
