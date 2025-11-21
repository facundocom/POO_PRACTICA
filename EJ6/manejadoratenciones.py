import csv
import numpy as np
from paciente import Paciente
from atenciones import Atenciones

class ManejadorAtenciones:
    __cant:int
    __dimension:int 
    __incremento:int
    __listaA:np.ndarray
    
    def __init__(self,dimension=10,incremento=1):
        self.__cant=0
        self.__dimension=dimension
        self.__incremento=incremento
        self.__listaA=np.empty(self.__dimension,dtype=Atenciones)

    def agregarAtencion(self,unaAtencion):
        if self.__cant==self.__dimension:
            print("Espacio de almacenamiento solicitado.")
            self.__dimension+=self.__incremento
            self.__listaA.resize(self.__dimension)
        self.__listaA[self.__cant]=unaAtencion
        self.__cant+=1

    def cargarAtenciones(self):
        archivo=open("atenciones.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                dni=int(fila[0])
                fechaatencion=fila[1]
                importeatencion=float(fila[2])
                atencion=Atenciones(dni,fechaatencion,importeatencion)
                self.agregarAtencion(atencion)
                print("Atencion cargada.")
        archivo.close()
    
    def buscarFecha(self,fecha):
        cont=0
        impTotal=0
        for i in range(self.__cant):
            if self.__listaA[i].getfechaatencion()==fecha:
                cont+=1
                impTotal+=self.__listaA[i].getimporteatencion()
        if cont>0:
            print(f"Las atenciones realizadas en la fecha {fecha} fueron {cont}. Importe total a pagar: ${impTotal:.2f}.")
        else:
            print("No se registraron atenciones para la fecha ingresada.")

    def atencionesMostrar(self,dni):
        cont=0
        for i in range(self.__cant):
            if self.__listaA[i].getdni()==dni:
                cont+=1
        print(f"El paciente con DNI {dni} tiene {cont} atenciones.")

    def contarAtenciones(self,dni):
        cont=0
        for i in range(self.__cant):
            if self.__listaA[i].getdni()==dni:
                cont+=1
        return cont


    

