from dataclasses import dataclass
import numpy as np
import copy

ABATIDO = 0
NORMAL = 1
DESPLAZADO = 2

operadores = [
    # --- Fila 1 ---
    "DESPLAZAR_PILOTO", "ABATIR_COPILOTO", "NORMAL_COPILOTO", "NORMAL_PILOTO", "DESPLAZAR_COPILOTO"
    
    # --- Fila 2 ---
    # Asiento Doble (Izq + Centro)
    "ABATIR_F2_DOBLE", "NORMAL_F2_DOBLE",
    # Asiento Derecho
    "ABATIR_F2_DER", "NORMAL_F2_DER",
    
    # --- Fila 3 ---
    "ABATIR_F3_IZQ",  "NORMAL_F3_IZQ",
    "ABATIR_F3_DER",  "NORMAL_F3_DER"
]

@dataclass
class tEstado:
    asientos : list

    def __init__(self, asiento_inicial):
        self.asientos = asiento_inicial


def esValido(estado: tEstado, op: str) -> bool:
    match op:
        case "DESPLAZAR_PILOTO":
            if(estado.asientos[1][0] == NORMAL and estado.asientos[0][0] == NORMAL):
                return True
            
        case "NORMAL_COPILOTO":
            if(estado.asientos[0][1] == ABATIDO and estado.asientos[0][1] == DESPLAZADO):
                return True

        case "ABATIR_COPILOTO":
            if(estado.asientos[1][1] == ABATIDO and estado.asientos[0][1] == NORMAL):
                return True

        case "NORMAL_PILOTO":
            if(estado.asientos[0][0] == DESPLAZADO):
                return True
        
        case "DESPLAZAR_COPILOTO":
            if(estado.asientos[0][1] == NORMAL and estado.asientos[1][1] == NORMAL ):
                return True
        
        case "ABATIR_F2_DOBLE":
            if(estado.asientos[1][0] == NORMAL):
                return True
        
        case "NORMAL_F2_DOBLE":
            if(estado.asientos[1][0] == ABATIDO):
                return True
            
        case "ABATIR_F2_DER":
            if(estado.asientos[1][1] == NORMAL):
                return True
            
        case "NORMAL_F2_DER":
            if(estado.asientos[1][1] == ABATIDO):
                return True
            
        case "ABATIR_F3_IZQ":
            if(estado.asientos[2][0] == NORMAL): 
                return True
            
        case "NORMAL_F3_IZQ":
            if(estado.asientos[2][0] == ABATIDO): 
                return True
            
        case "ABATIR_F3_DER":
            if(estado.asientos[2][1] == NORMAL): 
                return True
            
        case "NORMAL_F3_DER":
            if(estado.asientos[2][1] == ABATIDO): 
                return True
    
def aplicaOperador(estado: tEstado, op: str) -> tEstado:
    # 1. Creamos la copia de seguridad para no romper el estado anterior
    nuevo_estado = copy.deepcopy(estado)
    
    # 2. Modificamos directamente sobre nuevo_estado.asientos
    match op:
        # --- FILA 1: PILOTO (Posición [0][0]) ---
        case "DESPLAZAR_PILOTO":
            nuevo_estado.asientos[0][0] = DESPLAZADO
            
        case "NORMAL_PILOTO":
            nuevo_estado.asientos[0][0] = NORMAL
            
        # --- FILA 1: COPILOTO (Posición [0][1]) ---
        case "ABATIR_COPILOTO":
            nuevo_estado.asientos[0][1] = ABATIDO
            
        case "DESPLAZAR_COPILOTO":
            nuevo_estado.asientos[0][1] = DESPLAZADO
            
        case "NORMAL_COPILOTO":
            nuevo_estado.asientos[0][1] = NORMAL

        # --- FILA 2 ---
        case "ABATIR_F2_DOBLE":
            nuevo_estado.asientos[1][0] = ABATIDO
        case "NORMAL_F2_DOBLE":
            nuevo_estado.asientos[1][0] = NORMAL
            
        case "ABATIR_F2_DER":
            nuevo_estado.asientos[1][1] = ABATIDO
        case "NORMAL_F2_DER":
            nuevo_estado.asientos[1][1] = NORMAL

        # --- FILA 3 ---
        case "ABATIR_F3_IZQ":
            nuevo_estado.asientos[2][0] = ABATIDO
        case "NORMAL_F3_IZQ":
            nuevo_estado.asientos[2][0] = NORMAL
            
        case "ABATIR_F3_DER":
            nuevo_estado.asientos[2][1] = ABATIDO
        case "NORMAL_F3_DER":
            nuevo_estado.asientos[2][1] = NORMAL

    return nuevo_estado


estado_inicial = tEstado([
    [DESPLAZADO, DESPLAZADO], # Fila 1: Piloto, Copiloto
    [NORMAL, NORMAL],         # Fila 2: Doble, Derecho
    [ABATIDO, ABATIDO]        # Fila 3: F3_Izq, F3_Der
])