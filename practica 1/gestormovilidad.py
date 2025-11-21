##Vidable Agustin
# E009-70 LSI
# 44317140

import csv
import numpy as np
from gasto import Gasto
import gestorgastos
from movilidad import Movilidad
from gestorgastos import GestorGasto

class GestorMovilidad:
    __cant:int
    __dimension:int 
    __incremento:int
    __listaM:np.ndarray
    
    def __init__(self,dimension=10,incremento=1):
        self.__cant=0
        self.__dimension=dimension
        self.__incremento=incremento
        self.__listaM=np.empty(self.__dimension,dtype=Movilidad)

    def agregarMovilidad(self,unaMovilidad):
        if self.__cant==self.__dimension:
            print("Espacio de almacenamiento solicitado.")
            self.__dimension+=self.__incremento
            self.__listaM.resize(self.__dimension)
        self.__listaM[self.__cant]=unaMovilidad
        self.__cant+=1

    def cargarMovilidad(self):
        archivo = open("movilidades.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                patente = fila[0]
                tipo = fila[1]
                capacidad = int(fila[2])
                importe = float(fila[3])
                marca = fila[4]
                modelo = fila[5]
                movilidad = Movilidad(patente, tipo, capacidad, importe, marca, modelo)
                self.agregarMovilidad(movilidad)  
                print("Movilidad cargada.")
        archivo.close()

    def listarMovilidadesAPagar(self, fecha):
        self.__listaM = sorted(self.__listaM[:self.__cant])  

        print(f"Listado de movilidades a pagar para la fecha {fecha}:")
        for movilidad in self.__listaM:
            total_gastos = 0
        
            print(f"Patente: {movilidad.getPatente()}, Marca: {movilidad.getMarca()}, Modelo: {movilidad.getModelo()}")
            print(f"Total a pagar: {total_gastos}")
