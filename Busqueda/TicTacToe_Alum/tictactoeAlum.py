from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import numpy as np

@dataclass
class Nodo:
    tablero: np.array
    vacias: int
    N: int

    def __init__(self, tablero: np.ndarray):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        self.vacias = len(np.where(tablero == 0))

    def __str__(self) -> str:
        # Función para representar el nodo en forma de cadena (se llama a esta función al hacer print). 
        # Se utiliza el diccionario para utilizar la visualización a través de simbolos

        visual = {1: "X", -1: "O", 0.0: " "}
        string = f"{' ----+----+----'}\n|"
        for i in range(self.tablero.shape[0]):
            for j in range(self.tablero.shape[1]):
                if self.tablero[i, j] == 0:
                    string += "    |"
                else:
                    string += f" {visual[self.tablero[i, j]]} |"
            if i == 2 and j == 2:
                string += f"\n ----+----+----\n"
            else:
                string += f"\n ----+----+----\n|"
        return f"{string}"



@dataclass
class Jugada:
    x: int
    y: int

    def __str__(self):
        return f"\nFila: ({self.x}, Col: {self.y})"

######
# Se crean todas las posibles jugadas para el for de rango (for jugada in jugadas)
jugadas = []
for i in range(0, 3):
    for j in range(0, 3):
        jugadas.append(Jugada(i, j))
######




""" Funciones complementarias
    * crearNodo
    * nodoInicial
    * opuesto
"""


def crearNodo(tablero):
    return Nodo(tablero)


def nodoInicial():
    tablero_inicial = np.zeros((3, 3))
    return Nodo(tablero_inicial)


def opuesto(jugador):
    return jugador * -1


""" Funciones Búsqueda MiniMax
    * aplicaJugada
    * esValida
    * terminal
    * utilidad
"""


def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    """Realiza una copia del nodo recibido como parámetro y aplica la jugada indicada,
    modificando para ello los atributos necesarios. Para esto, se tiene en cuenta qué
    jugador realiza la jugada.

    Args:
        actual (Nodo)
        jugada (Jugada)
        jugador (int)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, 
        puede mantener esta excepción. Quítela cuando implemente la función

    Returns:
        Nodo: Contiene la información del nuevo estado del juego.
    """
    nuevo = deepcopy(actual)
    i,j = jugada.x, jugada.y        

    nuevo.tablero[i][j] = jugador

    nuevo.vacias = nuevo.vacias - 1

    return nuevo
    

def esValida(actual: Nodo, jugada: Jugada) -> bool:
    """Comprueba si dada una Jugada, es posible aplicarla o no. Evite la instrucción 'jugada in jugadas'
    para la comprobación ya que no tiene por qué estar incluida una lista de posibles jugadas. Por tanto, 
    use las operaciones lógicas para verificar la validez de la jugada.

    Args:
        actual (Nodo)
        jugada (Jugada)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, 
        puede mantener esta excepción. Quítela cuando implemente la función

    Returns:
        bool: Devuelve True en caso de que pueda realizarse la Jugada, False en caso contrario
    """
    valido = False
    i,j = jugada.x, jugada.y
    if (i <= actual.N and i >= 0) and (j <= actual.N and j >= 0): # si esta entre los límites se hace la jugada
        if(actual.tablero[i][j] == 0.0): #casilla del tablero vacia
            valido = True

    return valido 

    raise NotImplementedError


def terminal(actual: Nodo) -> bool:
    """Comprueba si el juego se ha acabado, ya sea porque alguno de los jugadores ha ganado o bien porque no 
    sea posible realizar ningún movimiento más.

    Args:
        actual (Nodo)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, 
        puede mantener esta excepción. Quítela cuando implemente la función

    Returns:
        bool: Devuelve True en caso de Terminal, False en caso contrario
    """
    terminal = False
    if(actual.vacias == 0):
        return True
    for i in range(actual.N):
        if abs(sum(actual.tablero[i, :])== actual.N):
            return True
        if abs(sum(actual.tablero[:, i]) == actual.N):
            return True
    suma_diag_principal = sum(actual.tablero[i][i] for i in range(actual.N))
    if abs(suma_diag_principal) == actual.N:
        return True

    # Diagonal Secundaria (0,2), (1,1), (2,0)...
    suma_diag_secundaria = sum(actual.tablero[i][actual.N-1-i] for i in range(actual.N))
    if abs(suma_diag_secundaria) == actual.N:
        return True

    return terminal 
    raise NotImplementedError


def utilidad(nodo: Nodo) -> int:
    """La función de utilidad, también llamada objetivo, asigna un valor numérico al nodo recibido como parámetro.
    Por ejemplo, en un juego de 'Suma cero', se puede establecer que devuelve -100, 0, 100 en función de qué jugador gana o bien si hay un empate.

    Args:
        nodo (Nodo)

    Raises:
        NotImplementedError: Mientras que no termine de implementar esta función, 
        puede mantener esta excepción. Quítela cuando implemente la función.

    Returns:
        int: Valor de utilidad
    """
    raise NotImplementedError
