from manejadoratenciones import ManejadorAtenciones
from manejadorpacientes import ManejadorPacientes

def menu():
    print("MENU DE OPCIONES")
    print("1.Informar Atenciones y el importe en una fecha dada.")
    print("2.Contar Atenciones de un Paciente.")
    print("3.Listar Pacientes sin Atenciones.")
    print("4.Listar Pacientes Ordenados por Apellido.")
    print("5.Salir.")
    op=int(input("Ingrese una opcion: "))
    return op

if __name__=="__main__":
    manejadorPacientes=ManejadorPacientes()
    manejadorAtenciones=ManejadorAtenciones()
    manejadorPacientes.agregarPaciente()
    manejadorAtenciones.cargarAtenciones()
    op=menu()

    while op!=5:
        if op==1:
            fecha=input("Ingrese la fecha a buscar: ")
            manejadorAtenciones.buscarFecha(fecha)

        elif op==2:
            dni=int(input("Ingrese el DNI del paciente: "))
            manejadorAtenciones.atencionesMostrar(dni)

        elif op==3:
            manejadorPacientes.listarPacientesSinAtencion()

        elif op==4:
            manejadorPacientes.listarPacientesOrdenadosPorApellido()

        else:
            print("Opcion incorrecta.")

        op=menu()

    print("Fin del programa.")
