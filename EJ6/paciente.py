class Paciente:
    __dni:int
    __nombre:str
    __apellido:str
    __unidad:str

    def __init__(self,dni,nombre,apellido,unidad):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__unidad=unidad

    def __str__(self):
        return f"Paciente: {self.__nombre} {self.__apellido}, DNI: {self.__dni}, Unidad: {self.__unidad}"
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def __lt__(self,other):
        if self.__unidad==other.__unidad:
            return self.__apellido<other.__apellido
        return self.__unidad<other.__unidad
    
    def getUnidad(self):
        return self.__unidad
    

