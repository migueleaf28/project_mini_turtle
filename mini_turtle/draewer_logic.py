posicion_x = 0
posicion_y = 0

def adelante(pasos):
    global posicion_x, posicion_y
    print(" " * posicion_x + "-" * pasos + ">")
    posicion_x += pasos

def abajo(pasos):
    global posicion_x, posicion_y

    for i in range(pasos):
        print(" " * posicion_x + "|")
    
    print(" " * posicion_x + "V")

    posicion_y += pasos

def reiniciar():
    global posicion_x, posicion_y
    posicion_x = 0
    posicion_y = 0

