class Atenciones:
    __dni:int
    __fechaatencion:str
    __importeatencion:float

    def __init__(self,dni,fechaatencion,importeatencion):
        self.__dni=dni
        self.__fechaatencion=fechaatencion
        self.__importeatencion=importeatencion

    def getdni(self):
        return self.__dni
    
    def getfechaatencion(self):
        return self.__fechaatencion
    
    def getimporteatencion(self):
        return self.__importeatencion
    
    def __str__(self):
        return f"Atencion: {self.__fechaatencion}, DNI: {self.__dni}, Importe: {self.__importeatencion}"
    