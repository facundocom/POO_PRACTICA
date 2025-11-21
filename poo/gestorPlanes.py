from Planes import Plan
from Televisiones import Television
from Telefonicos import Telefonico
import csv

class GestorPlanes():
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarPlan(self):

        band: bool
        b=str(input("Desea ingresar un nuevo plan? (si/no)"))

        if b.lower() not in ("si", "no"):
            print ('Ingrese solo "si" o "no"')

        elif b=="si":
            band=True
            while band != False:
                    
                nombrecomp = str(input("Ingrese el nombre de la compañía:"))
                duracion = int(input("Ingrese la duración del plan en días:"))
                cobertura = str(input("Ingrese la cobertura (nacional/internacional):"))
                while cobertura.lower() not in ("nacional", "internacional"):
                    print ("Por favor ingrese únicamente 'nacional' o 'internacional'")
                    cobertura = str(input("Ingrese la cobertura (nacional/internacional):"))
                precio = float(input("Ingrese el precio base del plan:"))

                tipoplan= str(input("El plan es telefónico o de tv?"))
                while tipoplan.lower() not in ("telefonico", "tv"):
                    print ("Por favor ingrese únicamente 'telefonico' o 'tv'")
                    tipoplan= str(input("El plan es telefónico o de tv?"))

                if tipoplan == "tv":
                    if cobertura.lower()=="internacional":
                        cantcanalint = int(input("ingrese la cant de canales internacionales que posee"))
                        cantcanalnac = int(input("Ingrese la cantidad de canales nacionales:"))

                    else:
                        cantcanalint = 0
                        cantcanalnac = int(input("Ingrese la cantidad de canales nacionales:"))

                    unPlan = Television(nombrecomp, duracion, cobertura, precio, cantcanalint, cantcanalnac)
                    self.agregarTelevision(unPlan)

                else:
                        tipo= str(input("Ingrese el tipo de llamadas(local, int, largadist)"))
                        cantmin=int(input("Ingrese cantidad de minutos de llamada:"))
                        unPlan = Telefonico(nombrecomp, duracion, cobertura, precio, tipo, cantmin)
                        self.agregarTelefonico(unPlan)

                band = str(input("Desea ingresar un nuevo plan? (si/no)"))
        else:
            band=False

    def agregarTelefonico(self, unPlan):
            self.__lista.append(unPlan)
            print("Plan telefónico cargado.")

    def agregarTelevision(self, unPlan):
            self.__lista.append(unPlan)
            print("Plan de televisión cargado.")

    def cargarCSV(self):
        archivo = open('planes.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            primercolumna = fila[0].strip().lower()
            if primercolumna == "m":
                unPlan = Telefonico(fila[1], 
                                    int(fila[2]), 
                                    fila[3], 
                                    float(fila[4]), 
                                    fila[5], 
                                    int(fila[6])
                                )
                self.agregarTelefonico(unPlan)
            elif primercolumna=="t": 
                nacional = int(fila[5]) if len(fila) > 5 and fila[5] else 0
                internacional = int(fila[6]) if len(fila) > 6 and fila[6] else 0

                unPlan = Television(
                    fila[1], 
                    int(fila[2]), 
                    fila[3], 
                    float(fila[4]), 
                    nacional, 
                    internacional
                    )
                self.agregarTelevision(unPlan)
        archivo.close()

    def mostrarPosicion(self, pos):

        datos = self.__lista[pos-1]
        if isinstance(datos, Telefonico):
            print ("En la posición ingresada se encuentra un plan telefónico.")

        else:
            print ("En la posición ingresada se encuentra un plan de televisión.")
    
    def mostrarGeo(self, geo):

        cont=0
        for plan in self.__lista:
            if geo.lower() in plan.getCob():
                cont+=1

        print(f"La cantidad de planes que corresponden a dicha ubicación geográfica son {cont}")

    def mostrarCantidad(self, cantint):
        print(f"Compañías con al menos {cantint} canales internacionales:")
        for planes in self.__lista:
            if isinstance(planes, Television):
                print(f"DEBUG: {planes.getNom()} tiene {planes.getInt()} canales internacionales")
                try:
                    if planes.getInt() >= cantint:
                        print (planes.getNom())
                except AttributeError:
                    pass
    
    def mostrarTodo(self):

        for planes in self.__lista:
            planes.mostrarDatos()