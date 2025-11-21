from gestoEquipos import ListaEquipos
from gestorResultado import ListaResultados


def menu():

    op=1
    while op!=0:

        print("MENU")
        print("1-2-3")
        op1=int(input("ingrese una opcion"))

        if op1==1:
            GR.mostrar(GE)
        elif op1==2:
             GR.mostrarNombre(GE)
        elif op1==3:
             GR.actualizar(GE)

if __name__=="__main__":
        
        cant=int(input("ingrese cantidad a cargar"))
        GE=ListaEquipos()
        GR=ListaResultados(cant)
        GR.cargar()
        GE.cargar()
        menu()