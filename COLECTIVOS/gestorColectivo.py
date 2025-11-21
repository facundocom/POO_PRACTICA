import csv
import numpy as np
from colectivo import Colectivo

class ListaColectivo:
    __cantidad:int
    __dimension:int
    __incremento:int
    __listaCol:np.ndarray

    def __init__(self,dimension,incremento=5):
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
        self.__listaCol=np.empty(self.__dimension,dtype=Colectivo)
    
    def agregarColectivo(self,unColectivo):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaCol.resize(self.__dimension)

        self.__listaCol[self.__cantidad]=unColectivo
        self.__cantidad+=1
    
    def cargar(self):

        archivo=open("colectivos.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True

        for fila in reader:
            if bandera:
                bandera=False
            else:
                patente=fila[0]
                marca=fila[1]
                modelo=fila[2]
                capacidad=fila[3]
                dni=fila[4]
                km=35
                unColectivo=Colectivo(patente,marca,modelo,capacidad,dni)
                self.agregarColectivo(unColectivo)

        print("Los colectivos fueron cargados correctamente")
        archivo.close()

    def documento(self):
        dni =input("Ingresar el documento de un chofer: ")

        i=0
        encontrado=False

        while i < self.__cantidad and not encontrado:
            if self.__listaCol[i].getDocumento() == dni:
                patente=self.__listaCol[i].getPatente()
                encontrado=True
            else:
                i+=1

        if encontrado:
            patente=patente
        else:
            patente="NO"
            print("Documento incorrecto")
        return patente
    
    def recorrido(self,mt):
        acum=0
        for i in range(self.__cantidad):
            colectivo=self.__listaCol[i]

            tramo=mt.patente(colectivo)
            acum+= tramo.getKm()
            print(f"-------------------------------")

            gasto_combustible= (Colectivo.getConsumo() * acum ) / 100

            print(f"Total de km recorridos: {acum}")
            print(f"Gasto de combustible: {gasto_combustible}")
            print(f"Patente:{self.__listaCol[i].getPatente()}")
            print("----------------------------------------")


   