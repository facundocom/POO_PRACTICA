##Vidable Agustin
# E009-70 LSI
# 44317140

from gestorgastos import GestorGasto
from gestormovilidad import GestorMovilidad

def menu():
    print("-----------MENU DE OPCIONES-----------")
    print("1.Listar gastos de mobilidad")
    print("2.Listar gastos de totales por fecha")
    print("3.Listar movilidades a pagar por fecha")
    print("4.SALIR")
    op=int(input("Ingrese una opcion: "))
    return op

if __name__=="__main__":
    gestorGastos=GestorGasto()
    gestorMovilidad=GestorMovilidad()
    gestorGastos.cargarGasto()
    gestorMovilidad.cargarMovilidad()
    op=menu()

    while op!=4:
        if op==1:
            patente=input("Ingrese la patente a buscar: ")
            gestorGastos.listarGastosMovilidad(patente)

        elif op==2:
            fecha=input("Ingrese la fecha a buscar: ")
            gestorGastos.listarGastosTotales(fecha)

        elif op==3:
            fecha=input("Ingrese la fecha a buscar: ")
            gestorMovilidad.listarMovilidadesAPagar(fecha)

        else:
            print("Opcion incorrecta.")

        op=menu()

    print("Fin del programa.")



