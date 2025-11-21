class Conexiones:
    __id:int
    __ip:str
    __juego:str
    __fecha:str
    __horaInicio:int
    __horaFinal:int

    def __init__(self,id,ip,jue,fecha,ini,fin):
        self.__id=id
        self.__ip=ip
        self.__juego=jue
        self.__fecha=fecha
        self.__horaInicio=ini
        self.__horaFinal=fin

    def getID(self):
        return self.__id
    def getIP(self):
        return self.__ip
    def getJuego(self):
        return self.__juego
    def getFecha(self):
        return self.__fecha
    def getInicio(self):
        return self.__horaInicio
    def getFinal(self):
        return self.__horaFinal
    def getTotalH(self):
        total=self.__horaFinal - self.__horaInicio
        return total
    def mostrar2(self):
        print("Ip:         Juego            FECHA           INICIO          FIN ")
        print(f"{self.__ip}         {self.__juego}       {self.__fecha}         {self.__horaInicio}         {self.__horaFinal}")
    def __eq__(self,other):
        valor=False
        if self.getID()==other.getID():
            if self.getIP()!=other.getIP():
                if self.getFecha()==other.getFecha():
                    if self.getInicio()==other.getInicio():
                        valor=True
        return valor
    def __lt__(self, otro):
        retorno = None
        if self.getID() != otro.getID():
            retorno = self.getID() < otro.getID()
        elif self.getFecha() != otro.getFecha():
            retorno = self.getFecha() < otro.getFecha()
        elif self.getInicio() != otro.getInicio():
            retorno = self.getInicio() < otro.getInicio()
        else:
            retorno = self.getIP() < otro.getIP()
        return retorno
