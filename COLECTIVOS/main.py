from gestorColectivo import ListaColectivo
from gestorTramo import ListaTramo

if __name__=="__main__":
    op1=int(input("ingrese los colectivos a cargar"))
    colectivo=ListaColectivo(op1)
    tramos=ListaTramo()


    colectivo.cargar()
    tramos.cargar()

    opcion = -1

    print(" 1- Ejercicio 1 / 2-Ejercicio 2 / 3-Ejercicio 3")

    while opcion ==-1:

        menu = input("Ingresar opcion: ")

        if menu == '1':
            print("Ejercicio 1")
            tramos.listar(colectivo)

        elif menu == '2':
            print("Ejercicio 2")
            colectivo.recorrido(tramos)
        
        elif menu == '3':
            print("Ejercicio 3")
            tramos.distancia()

        elif menu == '0':
            opcion = 0
            print("Salir")
        else:
            print("Numero incorrecto, elija otro o pulse cero para salir")