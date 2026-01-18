from dataclasses import dataclass
import copy

operadores = ["2MD", "2CD", "1MD", "1CD", "1C1MD", "2MI", "2CI", "1MI", "1CI", "1C1MI"]

@dataclass
class tEstado:
    Izquierda: list
    barco: int
    Derecha: list

    def __init__(self, Izquierda, barco, Derecha):
        self.barco = barco
        self.Derecha = Derecha
        self.Izquierda = Izquierda

def testObjetivo(estado: tEstado) -> bool:
    if(estado.Derecha[1] == 3 and estado.Derecha[0] == 3):
        return True
    
def es_seguro(misioneros, canibales):
    # Si hay misioneros (m > 0) Y hay más caníbales que misioneros... ¡PELIGRO!
    if misioneros > 0 and canibales > misioneros:
        return False
    return True

def EsValido(op: str, estado: tEstado) -> bool:
    # Definimos las variables para facilitar la lectura
    # Izquierda[0] = Misioneros, Izquierda[1] = Caníbales
    # estado.barco == 0 (Izquierda), estado.barco == 1 (Derecha)
    
    match op:
        # --- MOVIMIENTOS HACIA LA DERECHA (Barco debe estar en 0) ---
        case "2MD": # 2 Misioneros a Derecha
            if estado.barco == 0 and estado.Izquierda[0] >= 2:
                # Comprobamos seguridad futura: (Izquierda - 2M, Derecha + 2M)
                if es_seguro(estado.Izquierda[0]-2, estado.Izquierda[1]) and \
                   es_seguro(estado.Derecha[0]+2, estado.Derecha[1]):
                    return True

        case "2CD": # 2 Caníbales a Derecha
            if estado.barco == 0 and estado.Izquierda[1] >= 2:
                # (Izquierda - 2C, Derecha + 2C)
                if es_seguro(estado.Izquierda[0], estado.Izquierda[1]-2) and \
                   es_seguro(estado.Derecha[0], estado.Derecha[1]+2):
                    return True

        case "1MD": # 1 Misionero a Derecha
            if estado.barco == 0 and estado.Izquierda[0] >= 1:
                if es_seguro(estado.Izquierda[0]-1, estado.Izquierda[1]) and \
                   es_seguro(estado.Derecha[0]+1, estado.Derecha[1]):
                    return True

        case "1CD": # 1 Caníbal a Derecha
            if estado.barco == 0 and estado.Izquierda[1] >= 1:
                if es_seguro(estado.Izquierda[0], estado.Izquierda[1]-1) and \
                   es_seguro(estado.Derecha[0], estado.Derecha[1]+1):
                    return True

        case "1C1MD": # 1 de cada a Derecha
            if estado.barco == 0 and estado.Izquierda[0] >= 1 and estado.Izquierda[1] >= 1:
                if es_seguro(estado.Izquierda[0]-1, estado.Izquierda[1]-1) and \
                   es_seguro(estado.Derecha[0]+1, estado.Derecha[1]+1):
                    return True

        # --- MOVIMIENTOS HACIA LA IZQUIERDA (Barco debe estar en 1) ---
        case "2MI": # 2 Misioneros a Izquierda
            if estado.barco == 1 and estado.Derecha[0] >= 2:
                # Comprobamos seguridad futura: (Izquierda + 2M, Derecha - 2M)
                if es_seguro(estado.Izquierda[0]+2, estado.Izquierda[1]) and \
                   es_seguro(estado.Derecha[0]-2, estado.Derecha[1]):
                    return True

        case "2CI": # 2 Caníbales a Izquierda
            if estado.barco == 1 and estado.Derecha[1] >= 2:
                if es_seguro(estado.Izquierda[0], estado.Izquierda[1]+2) and \
                   es_seguro(estado.Derecha[0], estado.Derecha[1]-2):
                    return True

        case "1MI": # 1 Misionero a Izquierda
            if estado.barco == 1 and estado.Derecha[0] >= 1:
                if es_seguro(estado.Izquierda[0]+1, estado.Izquierda[1]) and \
                   es_seguro(estado.Derecha[0]-1, estado.Derecha[1]):
                    return True

        case "1CI": # 1 Caníbal a Izquierda
            if estado.barco == 1 and estado.Derecha[1] >= 1:
                if es_seguro(estado.Izquierda[0], estado.Izquierda[1]+1) and \
                   es_seguro(estado.Derecha[0], estado.Derecha[1]-1):
                    return True

        case "1C1MI": # 1 de cada a Izquierda
            if estado.barco == 1 and estado.Derecha[0] >= 1 and estado.Derecha[1] >= 1:
                if es_seguro(estado.Izquierda[0]+1, estado.Izquierda[1]+1) and \
                   es_seguro(estado.Derecha[0]-1, estado.Derecha[1]-1):
                    return True
                    
    return False

def aplicaOperador(op: str, estado: tEstado) -> tEstado:
    nuevo = copy.deepcopy(estado)

    match op:
        # --- IDAS (De Izquierda a Derecha) ---
        case "2MD":
            nuevo.Izquierda[0] -= 2
            nuevo.Derecha[0] += 2
            nuevo.barco = 1
        case "2CD":
            nuevo.Izquierda[1] -= 2
            nuevo.Derecha[1] += 2
            nuevo.barco = 1
        case "1MD":
            nuevo.Izquierda[0] -= 1
            nuevo.Derecha[0] += 1
            nuevo.barco = 1
        case "1CD":
            nuevo.Izquierda[1] -= 1
            nuevo.Derecha[1] += 1
            nuevo.barco = 1
        case "1C1MD": # 1 Caníbal y 1 Misionero
            nuevo.Izquierda[0] -= 1
            nuevo.Izquierda[1] -= 1
            nuevo.Derecha[0] += 1
            nuevo.Derecha[1] += 1
            nuevo.barco = 1

        # --- VUELTAS (De Derecha a Izquierda) ---
        case "2MI":
            nuevo.Derecha[0] -= 2
            nuevo.Izquierda[0] += 2
            nuevo.barco = 0
        case "2CI":
            nuevo.Derecha[1] -= 2
            nuevo.Izquierda[1] += 2
            nuevo.barco = 0
        case "1MI":
            nuevo.Derecha[0] -= 1
            nuevo.Izquierda[0] += 1
            nuevo.barco = 0
        case "1CI":
            nuevo.Derecha[1] -= 1
            nuevo.Izquierda[1] += 1
            nuevo.barco = 0
        case "1C1MI":
            nuevo.Derecha[0] -= 1
            nuevo.Derecha[1] -= 1
            nuevo.Izquierda[0] += 1
            nuevo.Izquierda[1] += 1
            nuevo.barco = 0

    return nuevo

def heuristica(estado : tEstado)-> int:
    if(estado.Izquierda[0] + estado.Izquierda[1] == 1):
        return 1
    heuristica = (estado.Izquierda[0] + estado.Izquierda[1]) * 2 -3
    return heuristica