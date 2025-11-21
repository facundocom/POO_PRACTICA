from ControladorColectivo import ControladorColectivo
from ControladorTramo import ControladorTramo
from Tramo import Tramo

def menu():
    print("-----> MENU DE OPCIONES <-----")
    print("a. Ingresar DNI de un chofer y emitir un listado con los datos")
    print("b. Mostrar por cada colectivo la cantidad total de km recorridos y el gasto estimado en combustible para la cantidad total de km recorridos")
    print("c. Ingresar distancia para listar los datos de los tramos en los que los km recorridos superan la distancia dada")
    print("d. SALIR")
    op = (input("Ingresar una opcion: "))
    return op

if __name__=="__main__":
    cantidad = int(input("Ingresar cantidad: "))
    controladorColectivo = ControladorColectivo(cantidad)
    controladorTramo = ControladorTramo()
    controladorColectivo.cargarColectivo()
    controladorTramo.cargarTramo()

    op = menu()
    while op != "d":
        if op == "a":
            dni=int(input("Ingrese DNI de chofer a buscar: "))
            patente = controladorColectivo.buscarColectivo(dni)
            controladorTramo.mostrarTramos(patente)
        elif op == "b":
            controladorColectivo.mostrarKilometrosYGasto()
            # controladorColectivo.gastoEstimado()
        elif op == "c":
            dist=int(input("Ingrese la distancia deseada: "))
            Tramo._gt_(dist)
            controladorTramo.listarDatos(dist)
        else:
            print("Opcion incorrecta")
        
        op=menu()
    
    print("FIN.")