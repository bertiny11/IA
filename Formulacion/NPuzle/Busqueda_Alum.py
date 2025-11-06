from __future__ import annotations
from dataclasses import dataclass
import numpy as np
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
        if esValido(op, nodo.estado):
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

# # Implementar la búsqueda en profundidad
def DFS() -> None:
    abiertos = []
    cerrados = []
    sucesores = []
    actual = None

    # Inicializamos la pila con el estado inicial
    abiertos.append(NodoInicial())
    objetivo = False

    while abiertos and not objetivo:
        # Extraer el primer elemento (LIFO)
        actual = abiertos.pop(0)
        cerrados.append(actual)

        # Comprobamos si el estado actual es objetivo
        objetivo = testObjetivo(actual.estado)

        if not objetivo:
            # Expandir sucesores del estado actual
            sucesores = expandir(actual)

            # Insertar sucesores al principio de la lista (pila)
            # pero evitando duplicados en abiertos y cerrados
            nuevos = [s for s in sucesores if s not in abiertos and s not in cerrados]
            abiertos = nuevos + abiertos  # prioridad a los nuevos

    return objetivo
def buscarRepetidos2(actual, cerrados):
    for nodo in cerrados:
        if np.array_equal(nodo.estado.t, actual.estado.t):
            return True
    #....
def buscarRepetidos1(actual, abiertos):
    for nodo in abiertos:
        if np.array_equal(nodo.estado.t, actual.estado.t):
            return True
#     1. Búsqueda en Profundidad Limitada.
def DLS(limite: int) -> None:
    abiertos = []
    cerrados = []
    sucesores = []
    profundidad_actual = 0

    abiertos.append(NodoInicial())
    objetivo = False

    while abiertos and not objetivo:

        actual = abiertos.pop(0)
        cerrados.append(actual)

        
        objetivo = testObjetivo(actual.estado)

        if not objetivo and actual.profundidad < limite :

            sucesores = expandir(actual)
            
            if(buscarRepetidos2(actual, cerrados)):
                #si el nuevo sucesor no es el mismo que hemos tenido en cerrado lo añadimos
                #una vez comprobado que no está en cerados debemos de comprobar si es igual en abiertos 
                if(buscarRepetidos1(actual, abiertos)):
                    abiertos = sucesores + abiertos
                    profundidad_actual = 1;
            
    return objetivo

#     2. Búsqueda en Profundidad Limitada Iterativa.
    
def DLSI(limite_inicial: int):
    limite = limite_inicial
    while True:
        print(f"Probando con límite de profundidad: {limite}")
        if DLS(limite):
            print("Objetivo encontrado")
            return True
        limite += 1  # Incrementar límite y volver a intentar