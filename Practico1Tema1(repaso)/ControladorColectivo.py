import csv
import numpy as np
from Colectivo import Colectivo
from ControladorTramo import ControladorTramo

class ControladorColectivo:
    def __init__(self, cantidad):
        self.__colectivos = np.empty(cantidad, dtype=Colectivo)
        self.__indice = 0
        
    def cargarColectivo(self):
        archivo = open("Practico1Tema1(repaso)/colectivos.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                colectivo = Colectivo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
                self.__colectivos[self.__indice] = colectivo
                self.__indice += 1
        archivo.close()

    def buscarColectivo(self, dni):
        colectivos = self.__colectivos
        i = 0
        bandera = False
        while i < len(colectivos) and bandera == False:
            if colectivos[i].getDni() == dni:
                bandera = True
                colectivo = colectivos[i]
                return colectivo
            else:
                i+1
        print("No se encontró el colectivo")

    def mostrarKilometrosYGasto(self):
        colectivos = self.__colectivos
        for colectivo in colectivos:
            distanciaRecorrida = ControladorTramo.calcularDistancia(colectivo.getPatente())
            gasto = distanciaRecorrida * 0.35
            print("La distancia recorrida por el colectivo ", colectivo.getPatente(), " es: ", distanciaRecorrida, " y el gasto estimado para el colectivo ", colectivo, " es: ", gasto)

    # def gastoEstimado(self):
    #     colectivos = self.__colectivos
    #     for colectivo in colectivos:
    #         distanciaRecorrida = ControladorTramo.calcularDistancia(colectivo.getPatente())
    #         gasto = distanciaRecorrida * 0.35
    #         print("El gasto estimado para el colectivo ", colectivo, " es: ", gasto)
        

            


