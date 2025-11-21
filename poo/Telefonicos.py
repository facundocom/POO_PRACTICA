from Planes import Plan

class Telefonico(Plan):
    __tipo: str
    __cantidadmin: float

    def __init__(self, nombrecomp, duracion, cobertura, precio, tipo, cantidadmin):
        super().__init__(nombrecomp, duracion, cobertura, precio)
        self.__tipo=tipo
        self.__cantidadmin=cantidadmin
    
    def getTipo(self):
        return self.__tipo
    
    def getCant(self):
        return self.__cantidadmin
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print (f'Tipo de llamadas {self.__tipo}')
        print (f'Cantidad de minutos que posee {self.__cantidadmin}')

    def descuentos(self):
        importe = self.getPre()
        if self.getCob() == 'internacional':
            importe += importe*1.2
        else:
            importe+= importe*0.925
        return importe

    
