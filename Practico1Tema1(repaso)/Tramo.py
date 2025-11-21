class Tramo:
    __origen: str
    __destino: str
    __distancia: float
    __patenteColectivo: str

    def __init__(self, origen, destino, distancia, patente):
        self.__origen = origen
        self.__destino = destino
        self.__distancia = distancia
        self.__patenteColectivo = patente

    def getOrigen(self):
        return self.__origen
    
    def getDestino(self):
        return self.__destino
    
    def getDistancia(self):
        return self.__distancia
    
    def getPatente(self):
        return self.__patenteColectivo
    
    def _gt_(self, dist):
        return self.__distancia > dist