from Planes import Plan

class Television(Plan):
    __cantcanalnac: int
    __cantcanalint: int
    

    def __init__(self, nombrecomp, duracion, cobertura, precio, cantcanalnac, cantcanalint):
        super().__init__(nombrecomp, duracion, cobertura, precio)
        self.__cantcanalnac= cantcanalnac
        self.__cantcanalint= cantcanalint
        

    def getInt(self):
        return self.__cantcanalint
    
    def getNac(self):
        return self.__cantcanalnac
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print (f'Cantidad de canales internacionales {self.__cantcanalint}')
        print (f'Cantidad de canales nacionales {self.__cantcanalnac}')

    def descuentos(self):
        if self.getPre() >= 10:
            importe = self.getPre()
            importe += importe*1.15
        return importe