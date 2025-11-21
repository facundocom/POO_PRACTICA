class Equipo:
    __id:str
    __denominacion:str
    __presidente:str
    __puntos:int
    __golesFavor:int
    __golesContra:int
    __diferencia:int

    def __init__(self,id,den,pres,pun,fav,con,dif):
        self.__id=id
        self.__denominacion=den
        self.__presidente=pres
        self.__puntos=pun
        self.__golesFavor=fav
        self.__golesContra=con
        self.__diferencia=dif
    def getGolFav(self):
        return self.__golesFavor
    def getGolContra(self):
        return self.__golesContra
    def getDif(self):
        return self.__diferencia
    def getPuntos(self):
        return self.__puntos

    def getID(self):
        return self.__id
    def getDenominacion(self):
        return self.__denominacion
        
    def setpuntos(self,res):
        if res=="ganar":
            self.__puntos+=3
        elif res=="empatar":
            self.__puntos+=1
    def act(self,fav,contra):
        self.__golesFavor+=fav
        self.__golesContra+=contra
        self.__diferencia= fav-contra
        if fav>contra:
            self.__puntos+=3
        elif fav==contra:
            self.__puntos=1
    def mostrar(self):
        print(f"{self.__denominacion}---{self.__puntos}-----{self.__golesContra}")
    def __gt__(self, otro):  
        return self.__puntos > otro.__puntos
    

        
        