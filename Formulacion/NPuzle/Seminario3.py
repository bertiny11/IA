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

    
        


operadores = {8: "ARRIBA_A", 2: "ABAJO_A", 4: "IZQDA_A", 6: "DRCHA_A",8: "ARRIBA_B", 2: "ABAJO_B", 4: "IZQDA_B", 6: "DRCHA_B",8: "ARRIBA_C", 2: "ABAJO_C", 4: "IZQDA_C", 6: "DRCHA_C"}
# operadores2 = {8: "ARRIBA", 2: "ABAJO", 4: "IZQDA", 6: "DRCHA"}
# operadores3 = {8: "ARRIBA", 2: "ABAJO", 4: "IZQDA", 6: "DRCHA"}

#Formalizar

def testObjetivo(estado: tEstado) -> bool:
    objetivo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return np.array_equal(estado.matriz, objetivo)

def esValido(estado: tEstado, op: str) -> bool:
    
    # match operadores[op]:
    #     case "ARRIBA_A":
    #         if(estado.f[1] - 1 < 0):
    #             return False
    #         return fila_vacia > 0
    #     case "ABAJO":
    #         return fila_vacia < N - 1
    #     case "IZQDA":
    #         return col_vacia > 0
    #     case "DRCHA":
    #         return col_vacia < N - 1
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
            nuevoEstado.matriz[estado.f[1]+2, estado.c[1]] = 1
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]-1] = 1
            nuevoEstado.matriz[estado.f[1]+1, estado.c[1]+1] = 1
            nuevoEstado.f[1] = nuevoEstado.f[1]+1  # Actualizar la posición de la pieza A
        case "IZQDA_A":
            # Mover la pieza A hacia la izquierda
            pass

            
    #         nuevoEstado.matriz[fila_vacia, col_vacia] = nuevoEstado.matriz[pieza_fila, pieza_col]
    #         nuevoEstado.matriz[pieza_fila, pieza_col] = 0
            
    #         nuevoEstado.f[2] = pieza_fila
    #         nuevoEstado.c[2] = pieza_col
    #         nuevoEstado.f[0] = pieza_fila - 1
            
    #     case "ABAJO":
    #         fila_vacia = estado.f[2]
    #         col_vacia = estado.c[2]
    #         pieza_fila = estado.f[0]
    #         pieza_col = estado.c[0]
            
    #         nuevoEstado.matriz[fila_vacia, col_vacia] = nuevoEstado.matriz[pieza_fila, pieza_col]
    #         nuevoEstado.matriz[pieza_fila, pieza_col] = 0
            
    #         nuevoEstado.f[2] = pieza_fila
    #         nuevoEstado.c[2] = pieza_col
    #         nuevoEstado.f[0] = pieza_fila + 1
            
    #     case "IZQDA":
    #         fila_vacia = estado.f[2]
    #         col_vacia = estado.c[2]
    #         pieza_fila = estado.f[0]
    #         pieza_col = estado.c[0]
            
    #         nuevoEstado.matriz[fila_vacia, col_vacia] = nuevoEstado.matriz[pieza_fila, pieza_col]
    #         nuevoEstado.matriz[pieza_fila, pieza_col] = 0
            
    #         nuevoEstado.f[2] = pieza_fila
    #         nuevoEstado.c[2] = pieza_col
    #         nuevoEstado.c[0] = pieza_col - 1
            
    #     case "DRCHA":
    #         fila_vacia = estado.f[2]
    #         col