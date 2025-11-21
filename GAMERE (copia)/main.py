from gestorConexiones import GestorConexiones
from gestorGamer import GestorGamer



def menu():
    op=1
    while op!=0:
        print("1-2-3")
        opcion=int(input("Ingrese un numero"))
        if opcion==1:
            dni=int(input("Ingrese el DNI del gamer: "))
            GC.listar(GG,dni)
        elif opcion==2:
            GC.juego(GG)
        elif opcion==3:
            GG.listarSimultaneo(GC)
        else: print("ingrese una opcion valida")



if __name__=="__main__":
    GG=GestorGamer()
    GC=GestorConexiones(10)
    GC.carga()
    GG.carga()

    menu()