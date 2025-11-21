##Vidable Agustin
# E009-70 LSI
# 44317140

import csv
from gasto import Gasto

class GestorGasto:
    __gasto:list

    def __init__(self):
        self.__gasto=[]
    
    def cargarGasto(self):
        archivo=open("gastosAbril2025.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                patente=fila[0]
                fecha=fila[1]
                importe=float(fila[2])
                descripcion=fila[3]
                gasto=Gasto(patente,fecha,importe,descripcion)
                self.__gasto.append(gasto)
                print("Gasto cargado.")
        archivo.close() 

    def listarGastosMovilidad(self,patente):
            for i in range(len(self.__gasto)):
                if self.__gasto[i].getPatente()==patente:
                    print(self.__gasto[i])
                else:
                    print("Gasto de movilidad no encontrado.")

    def listarGastosTotales(self,fecha):
            total=0
            for i in range(len(self.__gasto)):
                if self.__gasto[i].getFecha()==fecha:
                    total+=self.__gasto[i].getImporte()
            print(f"El total de gastos para la fecha {fecha} es: {total}")
      
        