from dataclasses import dataclass
import random
import copy

operadores = ["Ladron_Izquierda", "Ladron_Derecha", "Extrae_Banco"]

@dataclass
class tEstado:
    fila: list
    Ladrones: int
    Banco: int

    def __init__ (self, fila):
        self.fila = fila
        self.Ladrones = 0
        self.Banco = 0

def estadoInicial(N: int)-> tEstado:
    fila = []
    for i in range(N):
        fila.append(random.randint(1,9))
    return tEstado(fila)

def Esvalido(estado: tEstado, op: str) -> bool:

    match op:
        case "Ladron_Izquierda": #En este caso los ladrones escogen el extremo izquierdo
            if (len(estado.fila) > 0):
                return True
        
        case "Ladron_Derecha":
            if (len(estado.fila) > 0):
                return True
            
        case "Extrae_Banco":
            if (len(estado.fila) > 0):
                return True
    return False

def aplicaOperador(estado: tEstado, op: str) -> tEstado:
    nuevo = copy.deepcopy(estado)

    match op:
        case "Ladron_Izquierda": #roba la bolsa de la izquierda
            dinero = nuevo.fila.pop(0)
            nuevo.Ladrones += dinero

        case "Ladron_Derecha":
            dinero = nuevo.fila.pop()
            nuevo.Ladrones += dinero

        case "Extrae_Banco":
            dinero = nuevo.fila.pop()
            nuevo.Banco += dinero

    return nuevo

def TestObjetivo(estado: tEstado)-> bool:
    if(len(estado.fila) == 0 and estado.Ladrones > estado.Banco):
        return True