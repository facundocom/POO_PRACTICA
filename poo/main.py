from gestorPlanes import GestorPlanes

def menu():
    print("\n-----MENÚ DE OPCIONES-----\n")
    print("5. CARGAR PLANES MANUALMENTE")
    print("6. CARGAR PLANES DESDE CSV")
    print("1. Dada una posición de la lista: Mostrar por pantalla qué tipo de plan se encuentra almacenado en dicha posición (usar la función isinstance()).")
    print("2. Leer por teclado una cobertura geográfica y contar y mostrar la cantidad de planes que corresponden a la misma")
    print("3. Ingresar por teclado una cantidad de canales internacionales y mostrar el /los nombres de las compañías que ofrecen una cantidad mayor o igual a la ingresada")
    print("4. Para todos los planes en la lista, mostrar: Tipo de plan, nombre de la compañía, duración del plan, cobertura geográfica e importe final. Este ítem debe resolverlo en la clase base.")
    
    print("0. Salir")
    return input("Opción: ")

if __name__ == "__main__":
    gp=GestorPlanes()
    
    band = False
    while band == False:
        op = menu()
        if op == "1":
            pos= int(input("Ingrese la posicion q quiere buscar: \n"))
            gp.mostrarPosicion(pos)
        elif op == "2":
            geo= str(input("Ingrese la geografica q quiere buscar: \n"))
            gp.mostrarGeo(geo)
        elif op == "3":
            canint=int(input("Ingrese la cantidad de canales internacionales que desea buscar: \n"))
            gp.mostrarCantidad(canint)
        elif op == "4":
            gp.mostrarTodo()
        elif op == "5":
            gp.agregarPlan()
        elif op == "6":
            gp.cargarCSV()
        elif op == "0":
            band = True
        else:
            print("Opción incorrecta.")