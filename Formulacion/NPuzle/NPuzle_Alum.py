import numpy as np

from dataclasses import dataclass


@dataclass
class tEstado:
    t: np.ndarray
    N: int
    fila: int
    col: int

    def __init__(self, tablero: np.ndarray) -> None:
        self.t = tablero
        self.fila, self.col = np.where(tablero == 0)
        self.N = tablero.shape[0]


operadores = {8: "ARRIBA", 2: "ABAJO", 4: "IZQDA", 6: "DRCHA"}


def estadoInicial() -> tEstado:
    return tEstado(np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]]))
    # return tEstado(np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]])) # Pruebe esta combinación tras haber comprobado la anterior


def estadoObjetivo() -> tEstado:
    return tEstado(np.array([[1, 2, 3], [0, 4, 5], [8, 7, 6]]))
    # return tEstado(np.array([[1, 3, 0], [8, 2, 4], [7, 6, 5]])) #Pruebe esta combinación tras haber comprobado la anterior

def aplicaOperador(op: int, estado: tEstado) -> tEstado:
    nuevo = tEstado(estado.t.copy()) # Nuevo objeto, copia del anterior

    # Completar el código necesario

    operadores = {8: "ARRIBA", 2: "ABAJO", 4: "IZQDA", 6: "DRCHA"}
        
    match operadores[op]:
        case "ARRIBA":
            nuevo.t[nuevo.fila, nuevo.col] = nuevo.t[nuevo.fila - 1, nuevo.col]
            nuevo.t[nuevo.fila - 1, nuevo.col] = 0
            nuevo.fila -= 1
        case "ABAJO":
            nuevo.t[nuevo.fila, nuevo.col] = nuevo.t[nuevo.fila + 1, nuevo.col]
            nuevo.t[nuevo.fila + 1, nuevo.col] = 0
            nuevo.fila += 1
        case "IZQDA":
            nuevo.t[nuevo.fila, nuevo.col] = nuevo.t[nuevo.fila, nuevo.col - 1]
            nuevo.t[nuevo.fila, nuevo.col - 1] = 0
            nuevo.col -= 1
        case "DRCHA":
            nuevo.t[nuevo.fila, nuevo.col] = nuevo.t[nuevo.fila, nuevo.col + 1]
            nuevo.t[nuevo.fila, nuevo.col + 1] = 0
            nuevo.col += 1

    #....

    return nuevo


def esValido(op: int, estado: tEstado) -> bool:
    valido = False

    # Completar el código necesario

    operadores = {8: "ARRIBA", 2: "ABAJO", 4: "IZQDA", 6: "DRCHA"}

    match operadores[op]:
        case "ARRIBA":
            if estado.fila > 0:
                valido = True
        case "ABAJO":
            if estado.fila < estado.N - 1:
                valido = True
        case "IZQDA":
            if estado.col > 0:
                valido = True
        case "DRCHA":
            if estado.col < estado.col -1:
                valido = True
    #....    
    
    return valido


def testObjetivo(estado: tEstado) -> bool:
    objetivo = False
    # Completar el código
    
    if np.array_equal(estado.t, estadoObjetivo().t):
        objetivo = True

    #....    
    return objetivo


def coste(operador: str, estado: tEstado) -> int:
    return 1
