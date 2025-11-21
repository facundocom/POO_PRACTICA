import csv
from Tramo import Tramo

class ControladorTramo:
    __tramos: list

    def __init__(self):
        self.__tramos = []

    def cargarTramo(self):
        archivo = open("Practico1Tema1(repaso)/tramos.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        if bandera:
            bandera = False
        else:
            for fila in reader:
                tramo = Tramo(fila[0], fila[1], float(fila[2], fila[3]))
                self.__tramos.append(tramo)
        archivo.close()

    def mostrarTramos(self, patente):
        tramos = self.__tramos
        acc = 0
        for tramo in tramos:
            if tramo.getPatente() == patente:
                acc = acc + tramo.getDistancia()
                print(tramo.getOrigen())
                print(tramo.getDestino())
                print(tramo.getDistancia())
                print(tramo.getPatente())
            else:
                print("No se encontraron tramos asociados a esa patente.")
                return
        print("Total de km recorridos: ", acc)

    def calcularDistancia(self, patente):
        tramos = self.__tramos
        acc = 0
        
        for tramo in tramos:
            if tramo.getPatente() == patente:
                acc = acc + tramo.getDistancia()
                return acc
            
    def listarDatos(self, dist):
        for tramo in self.__tramos:
            if tramo > dist:
                print(f"Origen: {tramo.getOrigen()}, Destino: {tramo.getDestino()}, Patente: {tramo.getPatente()}, KM: {tramo.getDistancia()}")