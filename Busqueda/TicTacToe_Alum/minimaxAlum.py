from tictactoeAlum import *

def PSEUDOminimax(nodo: Nodo) -> Nodo:
    # El agente inteligente (que se corresponde con MAX) hace el movimiento... ¿más beneficioso para MAX?
    mejorJugada = -1
    puntos = -2
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, 1)
            util = utilidad(intento)
            if util > puntos:
                puntos = util
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, 1)
    return nodo


def jugadaAdversario(nodo: Nodo) -> Nodo:
    # El usuario (que se corresponde con MIN) hace el movimiento si es válido.
    valida = False
    jugada = None
    while not valida:
        fila = int(input("Fila: "))
        col = int(input("Col: "))
        jugada = Jugada(fila, col)
        valida = esValida(nodo, jugada)
        if not valida:
            print("\n Intenta otra posicion del tablero \n")
    nodo = aplicaJugada(nodo, jugada, -1)
    return nodo


def minimax(nodo: Nodo) -> Nodo:
    # Mientras que no termine de implementar esta función, 
    #   puede mantener esta excepción. Quítela cuando implemente la función
    jugador = 1
    mejorJugada = jugadas[0]
    max = -10000
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, jugador)
            max_actual = valorMin(intento)
            if max_actual > max:
                max = max_actual
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, jugador)
    return nodo


def valorMin(nodo) -> int:
    # Mientras que no termine de implementar esta función, 
    #   puede mantener esta excepción. Quítela cuando implemente la función
    valor_min = 100000
    jugador = -1
    if terminal(nodo):
        valor_min = utilidad(nodo)
    else:
        valor_min = 10000
        for jugada in jugadas:
            if esValida(nodo, jugada):
                valor_min = min(valor_min, valorMax(aplicaJugada(nodo, jugada, jugador)))

    return valor_min


def valorMax(nodo) -> int:
    # Mientras que no termine de implementar esta función, 
    #   puede mantener esta excepción. Quítela cuando implemente la función
    valor_Max = -100000
    jugador = 1
    if terminal(nodo):
        valor_Max = utilidad(nodo)
    else:
        valor_Max = -100000
        for jugada in jugadas:
            if esValida(nodo, jugada):
                valor_Max = max(valor_Max, valorMin(aplicaJugada(nodo, jugada, jugador)))
                
    return valor_Max
