from equipos import Equipo
import csv

class ListaEquipos:
    __listaEqui:list

    def __init__(self):
        self.__listaEqui=[]


    def cargar(self):
        archivo=open("equipos.csv",encoding="utf-8")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                id=fila[0]
                den=fila[1]
                pres=fila[2]
                puntos=int(fila[3])
                golF=int(fila[4])
                golC=int(fila[5])
                dif= golF-golC
                equipo=Equipo(id,den,pres,puntos,golF,golC,dif)
                self.__listaEqui.append(equipo)
                print("equipo ingresado")
        archivo.close()

    def getDenominacion(self,id):
        i=0
        while i< len(self.__listaEqui):
            if self.__listaEqui[i].getID()==id:
                return self.__listaEqui[i].getDenominacion()
            else:
                i+=1
    def buscarNombre(self,nom):
        encontrado=False
        for lista in self.__listaEqui:
            if nom==lista.getDenominacion():
                    resultado=lista.getID()
                    encontrado=True
                    print("1")
        if not encontrado:
                resultado="NO"
        return resultado
    def actualizar(self,id,fav,con):
        i=0
        encontrado=False
        while i< len(self.__listaEqui) and not encontrado:
            if self.__listaEqui[i].getID()==id:
                self.__listaEqui[i].act(fav,con)
                encontrado=True
            else:
                i+=1
    def mostrar(self):
         for lista in self.__listaEqui:
             lista.mostrar()
    def tabla(self):
            self.__listaEqui = sorted(self.__listaEqui, reverse=True)
            i=0
            for lista in self.__listaEqui:
                print("Pos  Equipos        Puntos      GF          GC      DF")
                print(f"  {i+1}  {lista.getDenominacion()}        {lista.getPuntos()}      {lista.getGolFav()}           {lista.getGolContra()}        {lista.getDif()}")   
                i+=1
             
    
    