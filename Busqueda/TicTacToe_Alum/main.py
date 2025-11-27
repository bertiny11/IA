from minimaxAlum import *

ganador:int = 0
jugador = int(input("Introduzca el 1er jugador: 1 IA, 2 Tú "))

if jugador != 1:
    jugador = -1

juego = nodoInicial()
while juego.vacias > 0 and not ganador:
    if jugador == 1:
        juego = PSEUDOminimax(juego)
    else:
        juego = jugadaAdversario(juego)
    print(juego)
    if terminal(juego):
        ganador = utilidad(juego)
    jugador = opuesto(jugador)

match ganador:
    case 0:
        print("EMPATE")
    case 100:
        print("GANA MAX (IA)")
    case -100:
        print("GANA MIN (JUGADOR)")
