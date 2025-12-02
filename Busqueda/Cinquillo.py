from dataclasses import dataclass
from copy import deepcopy
import numpy as np

#Constantes
MAX = 1
MIN = -1
MESA = 3
N = 10 #numeros de cartas
P = 2 # numero de palos
opts = {1: "MAX ", -1:"MIN ", 3: "MESA "}
palos = {0: "OROS ", 1: "BASTOS "}

@dataclass
class tJugada:
    Numero : int
    Palo : str

@dataclass
class tNodo:
    Cartas_max : int
    Cartas_Min : int
    mesa : list
    cartas: np.ndarray = np.zeros((P, N))
    #mesa

    def __init__(self, cartas_max: tJugada, cartas_min: tJugada, mesa: list):
        self.Cartas_max = cartas_max
        self.Cartas_Min = cartas_min
        self.mesa = mesa


def esValido(actual: tNodo, jugador: int, j: tJugada)-> bool:
    valida = False
    if jugador == MAX:
        if actual.cartas[j.Palo][j.Numero] == 1:
            if j.Numero == 5:
                valida = True
            elif j.Numero < 5:
                valida = actual.cartas[j.Palo][j.Numero +1] == MESA
            elif j.Numero > 5:
                valida = actual.cartas[j.Palo][j.Numero -1] == MESA
    return valida

def JugadaValida(actual: tNodo, jugador: int, jugada: tJugada)-> tNodo:
    nuevo = deepcopy(actual)        
    nuevo.cartas[jugada.Palo][jugada.Numero] = MESA
    if jugador == MAX :
        nuevo.Cartas_max -= 1
    else:
        nuevo.Cartas_Min -= 1

    return nuevo

def utilidad():
    pass

def terminal(nodo: tNodo)-> int:
    utilidad = 0
    if nodo.Cartas_max == 0:
        utilidad = 100
    elif nodo.Cartas_Min == 0:
        utilidad = -100
    return utilidad
