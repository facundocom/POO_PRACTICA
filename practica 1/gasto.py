##Vidable Agustin
# E009-70 LSI
# 44317140

class Gasto:
    __patente: str
    __fecha: str
    __importe: float
    __descripcion: str

    def __init__(self, patente: str, fecha: str, importe: float, descripcion: str):
        self.__patente = patente
        self.__fecha = fecha
        self.__importe = importe
        self.__descripcion = descripcion

    def __str__(self):
        return f"Patente: {self.__patente}, Fecha: {self.__fecha}, Importe: {self.__importe}, Descripcion: {self.__descripcion}"

    def getPatente(self):
        return self.__patente

    def getFecha(self):
        return self.__fecha

    def getImporte(self):
        return self.__importe

    def getDescripcion(self):
        return self.__descripcion
    
    def __lt__(self, other):
        if self.__fecha==other.__fecha:
            return self.__patente<other.__patente
        return self.__fecha<other.__fecha