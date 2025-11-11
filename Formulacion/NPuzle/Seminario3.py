import numpy as np
import copy
from dataclasses import dataclass


@dataclass
class tEstado:
    matriz: np.ndarray #tablero
    f: list #filas donde se encuentra el centro de la pieza
    c: list #columnas donde se encuentra el centro de la pieza
    N: int #tamaño del tablero

    def __init__(self, tablero, filas, cols):
        self.matriz = tablero
        self.f = filas
        self.c = cols

    
        


operadores = {8: "ARRIBA_A", 2: "ABAJO_A", 4: "IZQDA_A", 6: "DRCHA_A",8: "ARRIBA_B", 2: 
                "ABAJO_B", 4: "IZQDA_B", 6: "DRCHA_B",8: "ARRIBA_C", 2: "ABAJO_C", 4: "IZQDA_C", 6: "DRCHA_C"}


#Formalizar

def testObjetivo(estado: tEstado) -> bool:
    objetivo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return np.array_equal(estado.matriz, objetivo)

def esValido(estado: tEstado, op: str) -> bool:
    
    match operadores[op]:
        case "ARRIBA_A":
            if(estado.matriz[estado.f]-2, [estado.c] > 0):
                return True
        case "Abajo_A":
            if(estado.matriz[estado.f]+2, [estado.c] < estado.n):
                return True
        case "IZQDA_A":
            if(estado.matriz[estado.f], [estado.c]-2 > 0):
                return True
        case "DRCHA_A":
            if(estado.matriz[estado.f], [estado.c]+2 < estado.N):
                return True
        case "ARRIBA_B":
            if(estado.matriz[estado.f]-2, [estado.c] > 0):
                return True
        case "Abajo_B":
            if(estado.matriz[estado.f]-1, [estado.c] < estado.N):
                return True
        case "IZQDA_B":
            if(estado.matriz[estado.f], [estado.c]-2 > 0):
                return True
        case "DRCHA_B":
            if(estado.matriz[estado.f], [estado.c]+2 < estado.N):
                return True
        case "ARRIBA_C":
            if(estado.matriz[estado.f]-2, [estado.c] > 0):
                return True
        case "Abajo_C":
            if(estado.matriz[estado.f]+2, [estado.c] < estado.N):
                return True
        case "IZQDA_C":
            if(estado.matriz[estado.f], [estado.c]-1 > 0):
                return True
        case "DRCHA_A":
            if(estado.matriz[estado.f], [estado.c] > estado.N):
                return True

    return False

def aplicaOperador(op: str, estado: tEstado) -> tEstado:
    nuevoEstado = copy.deepcopy(estado)
    
    match operadores[op]:
        case "ARRIBA_A":
            # Mover la pieza A hacia arriba
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[1], estado.c[1]-1] = 0
            nuevoEstado.matriz[estado.f[1], estado.c[1]+1] = 0
            nuevoEstado.matriz[estado.f[1]-2, estado.c[1]] = 1
            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]-1] = 1
            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]+1] = 1
            
            nuevoEstado.f[1] = nuevoEstado.f[1]-1  # Actualizar la posición de la pieza A
        case "ABAJO_A":
            # Mover la pieza A hacia abajo
            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[1], estado.c[1]-1] = 0
            nuevoEstado.matriz[estado.f[1], estado.c[1]+1] = 0

            nuevoEstado.matriz[estado.f[1]+2, estado.c[1]] = 1
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]-1] = 1
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]+1] = 1
            nuevoEstado.f[1] = nuevoEstado.f[1]+1  # Actualizar la posición de la pieza A
        case "IZQDA_A":
            # Mover la pieza A hacia la izquierda
            nuevoEstado.matriz[estado.f[1], estado.c[1]+1] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]] = 0
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]] = 0

            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]-1] = 1
            nuevoEstado.matriz[estado.f[1], estado.c[1]-2] = 1
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]-1] = 1
            nuevoEstado.c[1] = nuevoEstado.c[1]-1  # Actualizar la posición de la pieza A
        case "DRCHA_A": 
            # Mover la pieza A hacia la derecha
            nuevoEstado.matriz[estado.f[1], estado.c[1]-1] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]] = 0
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]] = 0

            nuevoEstado.matriz[estado.f[1]-1, estado.c[1]+1] = 1
            nuevoEstado.matriz[estado.f[1], estado.c[1]+2] = 1
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]+1] = 1
            nuevoEstado.c[1] = nuevoEstado.c[1]+1  # Actualizar la posición de la pieza A
        
        case "ARRIBA_B":
            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[2], estado.c[2]-1] = 0
            nuevoEstado.matriz[estado.f[2], estado.c[2]+1] = 0

            nuevoEstado.matriz[estado.f[2]-2, estado.c[2]] = 1
            nuevoEstado.matriz[estado.f[2]-1, estado.c[2]-1] = 1
            nuevoEstado.matriz[estado.f[2]-1, estado.c[2]+1] = 1
            nuevoEstado.f[2] = nuevoEstado.f[2]-1  # Actualizar la posición de la pieza B
        case "ABAJO_B":
            nuevoEstado.matriz[estado.f[2], estado.c[2]-1] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[2], estado.c[2]+1] = 0
            nuevoEstado.matriz[estado.f[2]-1, estado.c[2]] = 0

            nuevoEstado.matriz[estado.f[2]+1, estado.c[2]] = 1
            nuevoEstado.matriz[estado.f[2]+1, estado.c[2]+1] = 1
            nuevoEstado.matriz[estado.f[2]+1, estado.c[2]-1] = 1
            nuevoEstado.f[2] = nuevoEstado.f[2]+1  # Actualizar la posición de la pieza B
        case "IZQDA_B":
            nuevoEstado.matriz[estado.f[2]-1, estado.c[2]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[2], estado.c[2]+1] = 0

            nuevoEstado.matriz[estado.f[2]-1, estado.c[2]-1] = 1
            nuevoEstado.matriz[estado.f[2], estado.c[2]-2] = 1
            nuevoEstado.c[2] = nuevoEstado.c[2]-1  # Actualizar la posición de la pieza B
        case "DRCHA_B":
            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 0
            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 0

            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 1
            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 1
            nuevoEstado.matriz[estado.f[2], estado.c[2]] = 1
            nuevoEstado.c[2] = nuevoEstado.c[2]+1  # Actualizar la posición de la pieza B
        case "ARRIBA_C":
            nuevoEstado.matriz[estado.f[3]+1, estado.c[3]] = 0  # Actualizar la matriz

            nuevoEstado.matriz[estado.f[3]-2, estado.c[3]] = 1
            nuevoEstado.f[3] = nuevoEstado.f[3]-1  # Actualizar la posición de la pieza C
        case "ABAJO_C":
            nuevoEstado.matriz[estado.f[3]-1, estado.c[3]] = 0  # Actualizar la matriz

            nuevoEstado.matriz[estado.f[3]+2, estado.c[3]] = 1
            nuevoEstado.f[3] = nuevoEstado.f[3]+1  # Actualizar la posición de la pieza C
        case "IZQDA_C":
            nuevoEstado.matriz[estado.f[3], estado.c[3]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[3]-1, estado.c[3]] = 0
            nuevoEstado.matriz[estado.f[3]+1, estado.c[3]] = 0

            nuevoEstado.matriz[estado.f[3], estado.c[3]-1] = 1
            nuevoEstado.matriz[estado.f[3]-1, estado.c[3]-1] =  1
            nuevoEstado.matriz[estado.f[3]+1, estado.c[3]-1] = 1

            nuevoEstado.c[3] = nuevoEstado.c[3]-1  # Actualizar la posición de la pieza C
        case "DRCHA_C":
            nuevoEstado.matriz[estado.f[3], estado.c[3]] = 0  # Actualizar la matriz
            nuevoEstado.matriz[estado.f[3]-1, estado.c[3]] = 0
            nuevoEstado.matriz[estado.f[3]+1, estado.c[3]] = 0

            nuevoEstado.matriz[estado.f[3], estado.c[3]+1] = 1
            nuevoEstado.matriz[estado.f[3]-1, estado.c[3]+1] = 1
            nuevoEstado.matriz[estado.f[3]+1, estado.c[3]+1] = 1  

            nuevoEstado.c[3] = nuevoEstado.c[3]+1  # Actualizar la posición de la pieza C

    return nuevoEstado

def testObjetivo(estado: tEstado) -> bool:
    objetivo = np.array()
    return np.array_equal(estado.matriz, objetivo)

def estadoOnjetivo():
    return tEstado(np.array()) [[-1,0,0,0,0,0],
                                [-1,0,0,0,0,0]
                                [0,0,0,0,0,0]
                                [0,1,0,-1,0,1]
                                [1,1,1,1,0,1]
                                [0,1,1,1,1,1]]
    
#Usamos la distancia de manhattan, ya que sabemos los centros de las figuras
def Heuristica1(estado: tEstado):#Debemos primero comprobar la distancia que hay desde el centro de las figuras hasta el centro de las figuras de su estado final
    obj = estadoOnjetivo()
    filas = np.abs(np.array(estado.f)[1:])
    columnas = np.abs(np.array(estado.c[1:]))
def Heuristica2():
    pass

#f(n) = h(n)
#hay que ordenar nuestra lista de abierto 
def Voraz():
    pass

def Estrella():
    pass