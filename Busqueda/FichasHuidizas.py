import numpy as np
import copy
from dataclasses import dataclass

@dataclass
class Nodo:
    tablero: np.array
    Negras: list #filas donde se encuentra el centro de la piezas negras y blancas
    Blancas: list #columnas donde se encuentra el centro de la piezas negras y blancas
    N: int #tamaño del tablero

class Jugada:
    ficha: int
    mov: int 

def aplicaJugada(actual: Nodo, jugador: int, jugada: Jugada)-> Nodo:
        nuevo = copy.deepcopy(actual)
        #suponemos que el movimiento ya es valido
        if jugador == MAX:
            fila, colu = nuevo.Blancas[jugada.ficha-1] 
            nuevo.tablero[fila][colu] = 0


def esValida(actual: Nodo, jugador: int, j: Jugada) -> bool:
    valida = False
    if jugador == MAX:
        fila, coli = actual.Negras[j.ficha-1]

        match j.mov:
            case arriba: 
                pass


def terminal(nodo: Nodo):
    u = 100
    if nodo.Negras[0][1] == N and nodo.Negras[1][1] == N:
        u = u
    elif nodo.Blancas[0][0] == N and nodo.Blancas[1][0] == 0:
        u = u*-1
    else:
        u = u*0
    
    

    return u 
#constantes
MAX = 1
MIN = .1
N = 3
NUM_FICHAS = 2
Moves = {1, "arriba", 2, "abajo", 3, "derecha", 4, "arribaB", 5, "derechaB", 6, "izquiedaB"}

