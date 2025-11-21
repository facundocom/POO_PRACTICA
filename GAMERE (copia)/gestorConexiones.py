from Conexiones import Conexiones
import csv
import numpy as np

class GestorConexiones:
    __cantidad:int
    __dimension:int
    __incremento:int
    __listaCon:np.ndarray

    def __init__(self,dim,cant=0,inc=5):
        self.__cantidad=cant
        self.__dimension=dim
        self.__incremento=inc
        self.__listaCon=np.empty(self.__dimension,dtype=Conexiones)

    def agregar(self,conexion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaCon.resize(self.__dimension)
        self.__listaCon[self.__cantidad]=conexion
        self.__cantidad+=1

    def carga(self):
        archivo=open("conexiones.csv",encoding="utf-8")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                 bandera=False
            else:
                id=int(fila[0])
                ip=fila[1]
                juego=fila[2]
                fecha=fila[3]
                inicio=int(fila[4])
                final=int(fila[5])
                conexion=Conexiones(id,ip,juego,fecha,inicio,final)
                self.agregar(conexion)
        archivo.close()
    def listar(self,gg,gamer):
        res=gg.buscar(gamer)
        total=0
        if res!=0:
            for i in range(self.__cantidad):
                if self.__listaCon[i].getID()==res:
                    gg.mostrar(res)
                    self.__listaCon[i].mostrar2()
                    total+=self.__listaCon[i].getFinal() - self.__listaCon[i].getInicio()
            exceso=gg.exceso(total,res)
            print(f"TotalH:{total}  Exceso:{exceso}")
            print(f"Importe Total: {gg.importe(res,exceso)}")
    """En el programa principal, leer por teclado el nombre de un juego, si no existe, mostrar un mensaje 
que advierta de tal situación, si existe, mostrar: dirección IP de conexión, nombre y apellido, alias, tipo 
de plan de los usuarios que han jugado dicho juego."""
    def juego(self,gg):
        juegoBuscar=input("ingrese juego a buscar")
        encontrado=False
        for i in range(self.__cantidad):
            if self.__listaCon[i].getJuego()==juegoBuscar:
                id=self.__listaCon[i].getID()
                encontrado=True
                print(self.__listaCon[i].getIP())
                gg.mostrarJuego(id)
        if not encontrado:
            print("No existe ese juego")

    def ordenar(self):
        self.__listaCon.sort()
    def listadoBasicos(self, xid):
        bandera = False
        i = 0
        for i in range(self.__cantidad):
            conexionA = self.__listaCon[i]
            if conexionA.getID() == xid:
                for j in range(self.__cantidad):
                    if i != j:
                        conexionB = self.__listaCon[j]
                        if conexionB.getID() == xid and conexionA == conexionB:
                                bandera = True
        return bandera


