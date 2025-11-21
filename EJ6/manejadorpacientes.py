import csv
from paciente import Paciente
from manejadoratenciones import ManejadorAtenciones

class ManejadorPacientes:
    __pacientes:list

    def __init__(self):
        self.__pacientes=[]
    
    def agregarPaciente(self):
        archivo=open("pacientes.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                dni=int(fila[0])
                apellido=fila[1]
                nombre=fila[2]
                unidad=fila[3]
                paciente=Paciente(dni,apellido,nombre,unidad)
                self.__pacientes.append(paciente)
                print("Paciente cargado.")
        archivo.close() 

    def listarPacientesSinAtencion(self):
        hayPacientes=False
        print("Listado de pacientes sin atencion: ")
        for paciente in self.__pacientes:
                dni=int(paciente.getDNI())
                cantAtenciones = ManejadorAtenciones().contarAtenciones(dni)
                if cantAtenciones==0:
                    print(paciente)
                    hayPacientes=True
        if not hayPacientes:
            print("Listado vacio. No hay pacientes sin atencion.")

    def listarPacientesOrdenadosPorApellido(self):
        self.__pacientes.sort()
        print("Lista de pacientes ordenados por unidad y apellido: ")
        unidadActual=""
        for paciente in self.__pacientes:
            if paciente.getUnidad()!=unidadActual:
                unidadActual=paciente.getUnidad()
                print(f"\nUnidad: {unidadActual}")
            print(paciente)

            