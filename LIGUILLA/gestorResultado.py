from resultados import Resultado
import csv
import numpy as np

class ListaResultados:
    __cantidad:int
    __dimension:int
    __incremeto:int
    __listaRes:np.ndarray


    def __init__(self,dim,cant=0,inc=5):
        self.__cantidad=cant
        self.__incremeto=inc
        self.__dimension=dim
        self.__listaRes=np.empty(self.__dimension,dtype=Resultado)

    def agregar(self,resultado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremeto
            self.__listaRes.resize(self.__dimension)
        self.__listaRes[self.__cantidad]=resultado
        self.__cantidad+=1

    def cargar(self):
        archivo=open("resultados.csv", encoding="utf-8")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                fecha=fila[0]
                idL=fila[1]
                golL=int(fila[2])
                idV=fila[3]
                golV=int(fila[4])
                resultado=Resultado(fecha,idL,golL,idV,golV)
                self.agregar(resultado)
            print("Resultado cargado")
        archivo.close()
    
    """Leer por teclado una fecha, imprimir los equipos (denominación) con los resultados obtenidos 
en dicha fecha. Al final del listado el importe recaudado por inscripción de los equipos."""
    def mostrar(self,ge):
        fecha=input("ingrese la fecha a buscar")
        for i in range(self.__cantidad):
            if self.__listaRes[i].getFecha()==fecha:
                local=ge.getDenominacion(self.__listaRes[i].getIdLocal())
                visitante=ge.getDenominacion(self.__listaRes[i].getIdVis())
                self.__listaRes[i].mostrar(local,visitante)
    """Leer el nombre de un equipo, mostrar los resultados de los partidos de local que jugó, 
    indicando el nombre del equipo contrincante y el resultado. """
    def mostrarNombre(self,ge):
        nom=input("ingrese el nombre a buscar").title()
        idlocal=ge.buscarNombre(nom)
        if idlocal!="NO":
            for i in range(self.__cantidad):
                if idlocal==self.__listaRes[i].getIdLocal():
                    print(f"{nom}:{self.__listaRes[i].getGolLocal()}-{self.__listaRes[i].getGolVis()} {ge.getDenominacion(self.__listaRes[i].getIdVis())}")
                else:
                    i+=1
        else:
            print(f"Nombre no valido{nom}")
    
    def actualizar(self,ge):
        for i in range(self.__cantidad):
            ge.actualizar(self.__listaRes[i].getIdLocal(),self.__listaRes[i].getGolLocal(),self.__listaRes[i].getGolVis())  
            ge.actualizar(self.__listaRes[i].getIdVis,self.__listaRes[i].getGolVis(),self.__listaRes[i].getGolLocal())
       # ge.mostrar()
        ge.tabla()
    







