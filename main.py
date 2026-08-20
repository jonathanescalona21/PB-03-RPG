from jugador import Jugador
from mago import Mago
from objetos import Objeto


#Método principal

def main():
    
    #CREAR JUGADOR  
    nuevo_jugador = Jugador("Jonathan")

    #CREAR PJS
    magician= Mago("Lucifer", 10, 100, 80)

    #ASOCIAR JUGADOR CON EL PJ
    nuevo_jugador.seleccionar_personaje(magician)
    nuevo_jugador.mostrar_personaje()

    #ATAQUE DEL MAGO
    magician.atacar()

    #CREAR OBJETOS

    pocion = Objeto("Pocion de vida", "Consumible")
    staff = Objeto("Staff del Arcangel", "Arma")

    #AGREGAR AL INVENTARIO
    magician.inventario.agregar_objeto(pocion)
    magician.inventario.agregar_objeto(staff)

    #MOSTRAR INVENTARIO
    magician.inventario.mostrar_inventario()

if __name__== "__main__":
    main()