from gamer import Gamerr
import csv

class GestorGamer:
    __listaGamer:list

    def __init__(self):
        self.__listaGamer=[]

    def carga(self):
        archivo=open("gammers.csv", encoding="utf-8")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                id=int(fila[0])
                dni=int(fila[1])
                nom=fila[2]
                ap=fila[3]
                alias=fila[4]
                plan=fila[5]
                imp=int(fila[6])
                lim=int(fila[7])
                gamer=Gamerr(id,dni,nom,ap,alias,plan,imp,lim)
                self.__listaGamer.append(gamer)
        archivo.close()
    def buscar(self,gamer):
        i=0
        bandera=False
        while i<len(self.__listaGamer) and not bandera:
            if self.__listaGamer[i].getDNI()==gamer:
                resultado=self.__listaGamer[i].getID()
                bandera=True
            else:
                i+=1
        if  not bandera:
            print(f"No existe ese dni") 
            resultado=0
        return resultado
    def mostrar(self,id):
        for lista in self.__listaGamer:
            if lista.getID()==id:
                lista.mostrar()
    def exceso(self,total,id):
        for lista in self.__listaGamer:
            exceso=0
            if lista.getID()==id:
                if lista.getLimite()>= total:
                    exceso=0
                else:
                    exceso=total-lista.getLimite()
                return exceso
    def importe(self,id,e):
        for lista in self.__listaGamer:
            if lista.getID()==id:
                importe=lista.getImporte()
                if e!=0:
                    if lista.getPlan()=="Basico":
                        importe+=(importe*0.25)*e
                    elif lista.getPlan()=="Extendido":
                        importe+=(importe*0.30)*e
                    else:
                        importe+=(importe*0.40)*e
                return importe      
    def mostrarJuego(self,id):
        for lista in self.__listaGamer:
            if lista.getID()==id:
                print(f"Nombre:{lista.getNombre()},Apellido:{lista.getApellido()},Alias:{lista.getAlias()},Plan:{lista.getPlan()}")
    """La empresa, quiere advertir a los gammesr que utilizan el servicio Basico que no pueden conectarse 
simultáneamente a los juegos en más de una dirección IP, en la misma fecha y hora de inicio. Para ello 
le  solicita  a  usted  que  emita  un  listado  de  jugadores  con  servicio  Basico,  que se conectan en IPs 
distintas, simultáneamente.  
Regla de negocio: para implementar esta funcionalidad, debe sobrecargar el operador == (__eq__), 
en  la  clase  Conexión.  Se  considera  que  dos  conexiones  son  simultáneas,  cuando  siendo  el  mismo 
idJugador, tienen la misma fecha, la misma hora de inicio y la dirección IP de conexión es distinta. 
Para optimizar la funcionalidad también debe sobrecargar el operador mayor que (__lt__) en la clase 
Conexión, a efectos de ordenar el gestor de Conexiones de menor a mayor por idJugador, fecha, hora 
de inicio e IP de conexión"""
    def listarSimultaneo(self,gc):
        gc.ordenar()
        for lista in self.__listaGamer:
            if lista.getPlan()=="Basico":
                if gc.listadoBasicos(lista.getID()):
                    print(f"- {lista.getNombre()} {lista.getApellido()}")




        


            


