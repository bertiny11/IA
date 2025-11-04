from __future__ import annotations
from dataclasses import dataclass
from NPuzle_Alum import tEstado, esValido, aplicaOperador, estadoInicial, testObjetivo, operadores


@dataclass
class Nodo:
    estado: tEstado
    operador: str 
    costeCamino: int 
    profundidad: int
    padre: Nodo 

def NodoInicial() -> Nodo:
    return Nodo(estadoInicial(), "", 0, 0, None)   

def dispCamino(nodo: Nodo) -> None:
    lista = []
    aux = nodo
    
    print("Estado inicial: \n", estadoInicial().t, "\n")
    
    while aux.padre is not None:
        lista.append(aux)
        aux = aux.padre
        
    for nodo in lista[::-1]:
        if nodo.operador in operadores:
            print("Movimiento hacia: ", operadores[nodo.operador], "\n", nodo.estado.t)
            print()


def dispSolucion(nodo: Nodo):
    dispCamino(nodo)
    print("Profundidad: ", nodo.profundidad)
    print("Coste: ", nodo.costeCamino)

def expandir(nodo: Nodo) -> list:
    sucesores = []
    # Completar el código.
    #Para poder hacer el expandir, es necesario probar si el operador es válido, si es valido aplicamos el operador y creamos un nuevo nodo con el nuevo estado generado.
    for op in operadores:
        if esValido(nodo.estado, op):
            nuevoEstado = aplicaOperador(op, nodo.estado)
            nuevoNodo = Nodo(nuevoEstado, op, nodo.costeCamino + 1, nodo.profundidad + 1, nodo)
            sucesores.append(nuevoNodo)
    #....

    return sucesores

def BFS() -> None:
    objetivo = False

    raiz = NodoInicial()
    abiertos = []
    sucesores = []
    cerrados = []
    abiertos.append(raiz)

    # Completar el resto del código
    
    while len(abiertos) > 0 and not objetivo:
        raiz = abiertos.pop(0)
        cerrados.append(raiz)
        if testObjetivo(raiz.estado):
            objetivo = True
            dispSolucion(raiz)
        else:
            sucesores = expandir(raiz)
            for nodo in sucesores:
                if all(nodo.estado.t != c.estado.t for c in cerrados + abiertos):
                    abiertos.append(nodo)  
    # Completar
    if not objetivo:
        print("No se ha encontrado solución")

# Implementar la búsqueda en profundidad
    
    
    