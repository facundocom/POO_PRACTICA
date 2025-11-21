import csv
from tramo import Tramo
class ListaTramo:
    __listaTramo:list

    
    def __init__(self):
        self.__listaTramo=[]

    def cargar(self):

        archivo=open("tramos.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                ori=fila[0]
                des=fila[1]
                dis=int(fila[2])
                pat=fila[3]
                unTramo=Tramo(ori,des,dis,pat)
                self.__listaTramo.append(unTramo)
        print("SE CARGARON LOS TRAMOS CORRECTAMENTE")
        archivo.close()


    def listar(self,mc):
            pat=mc.documento()
            if pat!= "NO":
                totalkm=0
                for lista in self.__listaTramo:
                    if lista.getPatente()==pat:
                        totalkm=lista.getKm()
                        lista.Mostrar()
                print(f"Kilometros recorridos: {totalkm}")
    
    def patente(self,mc):

        i=0
        encontrado=False

        while i < len(self.__listaTramo) and not encontrado:
            if self.__listaTramo[i].getPatente() == mc.getPatente():
                encontrado=True
                pat= self.__listaTramo[i]
            else:
                i+=1
        
        return pat
    def distancia(self):
        op=int(input("Ingrese la distancia recorrida"))
        for lista in self.__listaTramo:
            if lista > op:
                lista.Mostrar()
       


