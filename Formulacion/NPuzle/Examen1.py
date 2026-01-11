from dataclasses import dataclass
import numpy as np
import copy

#apartado A
operadores = [
    "ARRIBA_A", "ABAJO_A", "IZQDA_A", "DRCHA_A",
    "ARRIBA_B", "ABAJO_B", "IZQDA_B", "DRCHA_B",
    "ARRIBA_C", "ABAJO_C", "IZQDA_C", "DRCHA_C"
]
#apartado B
@dataclass
class tEstado:
    matriz: np.ndarray #tablero
    N : int
    f : list
    c : list

    def __init__(self, tablero, filas, columnas):
        self.matriz = tablero
        self.f = filas
        self.c = columnas

#apartado C

def esValido(estado: tEstado, op: str) -> bool:
    f = estado.f[0] # Fila del centro de A
    c = estado.c[0] # Columna del centro de A
    
    # Nota: Asumimos que 0 es casilla vacía y != 0 es obstáculo

    match op:
        # --- MOVIMIENTOS PIEZA A (CRUZ) ---
        case "ARRIBA_A":
            # 1. Límite: Cabeza de la cruz
            if f - 2 >= 0:
                # 2. Obstáculos: Cabeza y los dos hombros
                if (estado.matriz[f-2][c] == 0 and 
                    estado.matriz[f-1][c-1] == 0 and 
                    estado.matriz[f-1][c+1] == 0):
                    return True
                    
        case "ABAJO_A":
            # 1. Límite: Pies de la cruz
            if f + 2 < estado.N:
                # 2. Obstáculos: Pies y bajo los sobacos
                if (estado.matriz[f+2][c] == 0 and 
                    estado.matriz[f+1][c-1] == 0 and 
                    estado.matriz[f+1][c+1] == 0):
                    return True

        case "IZQDA_A":
            # 1. Límite: Brazo izquierdo
            if c - 2 >= 0:
                # 2. Obstáculos: Punta izq, y los lados del brazo izq (arriba y abajo)
                if (estado.matriz[f][c-2] == 0 and 
                    estado.matriz[f-1][c-1] == 0 and 
                    estado.matriz[f+1][c-1] == 0):
                    return True

        case "DRCHA_A":
            # 1. Límite: Brazo derecho
            if c + 2 < estado.N:
                # 2. Obstáculos: Punta der, y los lados del brazo der
                if (estado.matriz[f][c+2] == 0 and 
                    estado.matriz[f-1][c+1] == 0 and 
                    estado.matriz[f+1][c+1] == 0):
                    return True

        # --- MOVIMIENTOS PIEZA B (La Pirámide) ---
        # Forma: Base de 3 abajo, punta en el centro arriba.
        # Centro (f, c): Casilla central de la base.
        
        case "ARRIBA_B":
            f, c = estado.f[1], estado.c[1]
            # Límite: La nueva punta de la pirámide (sube a f-2)
            if f - 2 >= 0:
                # Obstáculos: Nueva punta y los dos hombros de la nueva base
                if (estado.matriz[f-2][c] == 0 and 
                    estado.matriz[f-1][c-1] == 0 and 
                    estado.matriz[f-1][c+1] == 0):
                    return True

        case "ABAJO_B":
            f, c = estado.f[1], estado.c[1]
            # Límite: La nueva base (baja a f+1)
            if f + 1 < estado.N:
                # Obstáculos: Toda la base nueva (izq, centro, der)
                if (estado.matriz[f+1][c-1] == 0 and 
                    estado.matriz[f+1][c] == 0 and 
                    estado.matriz[f+1][c+1] == 0):
                    return True

        case "IZQDA_B":
            f, c = estado.f[1], estado.c[1]
            # Límite: El extremo izquierdo de la base (se mueve a c-2)
            if c - 2 >= 0:
                # Obstáculos: Nueva punta izq y nuevo extremo base izq
                if (estado.matriz[f-1][c-1] == 0 and 
                    estado.matriz[f][c-2] == 0):
                    return True

        case "DRCHA_B":
            f, c = estado.f[1], estado.c[1]
            # Límite: El extremo derecho de la base (se mueve a c+2)
            if c + 2 < estado.N:
                # Obstáculos: Nueva punta der y nuevo extremo base der
                if (estado.matriz[f-1][c+1] == 0 and 
                    estado.matriz[f][c+2] == 0):
                    return True

        # --- MOVIMIENTOS PIEZA C (La Barra Vertical) ---
        # Forma: Línea vertical de 3 casillas.
        # Centro (f, c): Casilla del medio.

        case "ARRIBA_C":
            f, c = estado.f[2], estado.c[2]
            # Límite: La cabeza (sube a f-2)
            if f - 2 >= 0:
                # Obstáculos: Solo la nueva cabeza
                if estado.matriz[f-2][c] == 0:
                    return True

        case "ABAJO_C":
            f, c = estado.f[2], estado.c[2]
            # Límite: Los pies (bajan a f+2)
            if f + 2 < estado.N:
                # Obstáculos: Solo los nuevos pies
                if estado.matriz[f+2][c] == 0:
                    return True

        case "IZQDA_C":
            f, c = estado.f[2], estado.c[2]
            # Límite: Columna izquierda (c-1)
            if c - 1 >= 0:
                # Obstáculos: Toda la columna nueva (arriba, medio, abajo)
                if (estado.matriz[f-1][c-1] == 0 and 
                    estado.matriz[f][c-1] == 0 and 
                    estado.matriz[f+1][c-1] == 0):
                    return True

        case "DRCHA_C":
            f, c = estado.f[2], estado.c[2]
            # Límite: Columna derecha (c+1)
            if c + 1 < estado.N:
                # Obstáculos: Toda la columna nueva
                if (estado.matriz[f-1][c+1] == 0 and 
                    estado.matriz[f][c+1] == 0 and 
                    estado.matriz[f+1][c+1] == 0):
                    return True
                
def aplicaOperador(estado: tEstado, op: str) -> tEstado:
    nuevoEstado = copy.deepcopy(estado)
    
    match op:
        case "ARRIBA_A":
            f = estado.f[0]
            c = estado.c[0]
            nuevoEstado.matriz[f+1][c] = 0
            nuevoEstado.matriz[f][c+1] = 0
            nuevoEstado.matriz[f][c-1] = 0
            nuevoEstado.matriz[f-2][c] = 1
            nuevoEstado.matriz[f-1][c+1] = 1
            nuevoEstado.matriz[f-1][c-1] = 1
            nuevoEstado.f[0] = f-1

        case "ABAJO_A":
            f, c = estado.f[0], estado.c[0]
            # 1. BORRAR: La parte de arriba que abandonamos
            #    (La cabeza vieja y los dos brazos viejos)
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f][c-1] = 0
            nuevoEstado.matriz[f][c+1] = 0
            
            # 2. PINTAR: La parte de abajo nueva
            #    (Los pies nuevos y los brazos nuevos, que han bajado una fila)
            nuevoEstado.matriz[f+2][c] = 2
            nuevoEstado.matriz[f+1][c-1] = 2
            nuevoEstado.matriz[f+1][c+1] = 2
            
            # 3. ACTUALIZAR: El centro baja una fila
            nuevoEstado.f[0] = f + 1

        case "IZQDA_A":
            f, c = estado.f[0], estado.c[0]
            # 1. BORRAR: La parte derecha que abandonamos
            #    (El brazo derecho viejo y las puntas vertical vieja arriba/abajo)
            nuevoEstado.matriz[f][c+1] = 0
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f+1][c] = 0
            
            # 2. PINTAR: La parte izquierda nueva
            #    (La punta izquierda nueva y las puntas verticales nuevas)
            nuevoEstado.matriz[f][c-2] = 2
            nuevoEstado.matriz[f-1][c-1] = 2
            nuevoEstado.matriz[f+1][c-1] = 2
            
            # 3. ACTUALIZAR: El centro se mueve a la izquierda
            nuevoEstado.c[0] = c - 1

        case "DRCHA_A":
            f, c = estado.f[0], estado.c[0]
            # 1. BORRAR: La parte izquierda que abandonamos
            nuevoEstado.matriz[f][c-1] = 0
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f+1][c] = 0
            
            # 2. PINTAR: La parte derecha nueva
            nuevoEstado.matriz[f][c+2] = 2
            nuevoEstado.matriz[f-1][c+1] = 2
            nuevoEstado.matriz[f+1][c+1] = 2
            
            # 3. ACTUALIZAR: El centro se mueve a la derecha
            nuevoEstado.c[0] = c + 1

        case "ARRIBA_B":
            f, c = estado.f[1], estado.c[1]
            # 1. BORRAR (Base vieja)
            nuevoEstado.matriz[f][c] = 0
            nuevoEstado.matriz[f][c-1] = 0
            nuevoEstado.matriz[f][c+1] = 0
            # 2. PINTAR (Nueva punta y hombros)
            nuevoEstado.matriz[f-2][c] = 1
            nuevoEstado.matriz[f-1][c-1] = 1
            nuevoEstado.matriz[f-1][c+1] = 1
            # 3. ACTUALIZAR
            nuevoEstado.f[1] = f - 1

        case "ABAJO_B":
            f, c = estado.f[1], estado.c[1]
            # 1. BORRAR (Punta vieja y extremos de la base vieja)
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f][c-1] = 0
            nuevoEstado.matriz[f][c+1] = 0
            # 2. PINTAR (Nueva base completa abajo)
            nuevoEstado.matriz[f+1][c-1] = 1
            nuevoEstado.matriz[f+1][c] = 1
            nuevoEstado.matriz[f+1][c+1] = 1
            nuevoEstado.f[1] = f + 1

        case "IZQDA_B":
            f, c = estado.f[1], estado.c[1]
            # 1. BORRAR (Punta vieja y extremo derecho base vieja)
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f][c+1] = 0
            # 2. PINTAR (Nueva punta izq y extremo izq base)
            nuevoEstado.matriz[f-1][c-1] = 1
            nuevoEstado.matriz[f][c-2] = 1
            nuevoEstado.c[1] = c - 1

        case "DRCHA_B":
            f, c = estado.f[1], estado.c[1]
            # 1. BORRAR (Punta vieja y extremo izquierdo base vieja)
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f][c-1] = 0
            # 2. PINTAR (Nueva punta der y extremo der base)
            nuevoEstado.matriz[f-1][c+1] = 1
            nuevoEstado.matriz[f][c+2] = 1
            nuevoEstado.c[1] = c + 1

        case "ARRIBA_C":
            f, c = estado.f[2], estado.c[2]
            # 1. BORRAR (El pie que sube)
            nuevoEstado.matriz[f+1][c] = 0
            # 2. PINTAR (La nueva cabeza que aparece arriba)
            nuevoEstado.matriz[f-2][c] = 1
            # 3. ACTUALIZAR
            nuevoEstado.f[2] = f - 1

        case "ABAJO_C":
            f, c = estado.f[2], estado.c[2]
            # 1. BORRAR (La cabeza que baja)
            nuevoEstado.matriz[f-1][c] = 0
            # 2. PINTAR (El nuevo pie que aparece abajo)
            nuevoEstado.matriz[f+2][c] = 1
            nuevoEstado.f[2] = f + 1

        case "IZQDA_C":
            f, c = estado.f[2], estado.c[2]
            # 1. BORRAR (Toda la columna derecha vieja)
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f][c] = 0
            nuevoEstado.matriz[f+1][c] = 0
            # 2. PINTAR (Toda la columna izquierda nueva)
            nuevoEstado.matriz[f-1][c-1] = 1
            nuevoEstado.matriz[f][c-1] = 1
            nuevoEstado.matriz[f+1][c-1] = 1
            nuevoEstado.c[2] = c - 1

        case "DRCHA_C":
            f, c = estado.f[2], estado.c[2]
            # 1. BORRAR (Toda la columna izquierda vieja)
            nuevoEstado.matriz[f-1][c] = 0
            nuevoEstado.matriz[f][c] = 0
            nuevoEstado.matriz[f+1][c] = 0
            # 2. PINTAR (Toda la columna derecha nueva)
            nuevoEstado.matriz[f-1][c+1] = 1
            nuevoEstado.matriz[f][c+1] = 1
            nuevoEstado.matriz[f+1][c+1] = 1
            nuevoEstado.c[2] = c + 1
    
    return nuevoEstado

def testObjetivo(estado: tEstado) -> bool:
    # Comparamos la matriz del estado actual con la matriz objetivo
    return np.array_equal(estado.matriz, estadoOnjetivo())

def estadoOnjetivo():
    # Definimos la matriz correctamente con comas separando las filas
    # y todo dentro de los paréntesis de np.array([ ... ])
    return np.array([
        [-1, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0],
        [ 0, 1, 0,-1, 0, 1],
        [ 1, 1, 1, 1, 0, 1],
        [ 0, 1, 1, 1, 1, 1]
    ])

def heuristica(estado: tEstado):
    return abs(estado.f[0]-4) + abs(estado.c[0]-1) + abs(estado.f[1]-5) + abs(estado.c[1]-3) + abs(estado.f[2]-4) + abs(estado.c[2]-5)