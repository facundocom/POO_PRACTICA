class Tramo:
    __origen:str
    __destino:str
    __distancia:int
    __patente:str

    def __init__(self,ori,des,dis,pat):
        self.__origen=ori
        self.__destino=des
        self.__distancia=dis
        self.__patente=pat

    def Mostrar(self):
        print(f"Origen: {self.__origen},Destino:{self.__destino},Distancia:{self.__distancia},Patente: {self.__patente}")
    def getKm(self):
        return self.__distancia
    def getPatente(self):
        return self.__patente
    def __gt__(self,other):
        return self.__distancia > other