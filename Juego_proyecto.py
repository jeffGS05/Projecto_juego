from random import randint

# Lista de opciones
t = ["Piedra", "Papel", "Tijera"]

#assign a random play to the computer
computadora = t[randint(0,2)]

#set jugador to False
jugador = False

while jugador == False:
#set jugador como True
    jugador = input("Piedra, Papel, Tijera? ")
    if jugador == computadora:
        print("Empate!")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("Perdiste!", computadora, "cubre", jugador)
        else:
            print("Ganaste!", jugador, "destruye", computadora)
    elif jugador == "Papel":
        if computadora == "Tijera":
            print("Perdiste!", computadora, "corta", jugador)
        else:
            print("Ganaste!", jugador, "cubre", computadora)
    elif jugador == "Tijera":
        if computadora == "Piedra":
            print("Perdiste...", computadora, "destruye", jugador)
        else:
            print("Ganaste!", jugador, "corta", computadora)
    else:
        print("Esa no es una opcion valida!")
    #jugador Esto esta como true, pero queremos que sea falso para que el loop continue
    jugador = False
    computadora = t[randint(0,2)]