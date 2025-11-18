from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from NPuzle_Alum import tEstado, esValido, aplicaOperador, estadoInicial, testObjetivo, operadores, heuristica

@dataclass
class Nodo:
    estado: tEstado
    operador: str 
    costeCamino: int 
    profundidad: int
    padre: Nodo 
    heuristica: int

    # def __lt__(self, other):
        # return self.heuristica < other.heuristica

    def __lt__(self, other):
        return (self.heuristica + self.costeCamino) < (other.heuristica + other.costeCamino)

def NodoInicial() -> Nodo:
    return Nodo(estadoInicial(), "", 0, 0, None, heuristica(estadoInicial()))   

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
            nuevoNodo = Nodo(nuevoEstado, op, nodo.costeCamino + 1, nodo.profundidad + 1, nodo, heuristica(nuevoEstado))
            sucesores.append(nuevoNodo)

    #....

    return sucesores

def BFS() -> None:
    objetivo = False

    raiz = NodoInicial()
    abiertos = []
    sucesores = []
    cerrados = set()

    # Completar el resto del código
    
    while len(abiertos) > 0 and not objetivo:
        raiz = abiertos.pop(0)
        cerrados.append(raiz)
        if testObjetivo(raiz.estado):
            objetivo = True
            dispSolucion(raiz)
            break
        if raiz.estado not in cerrados:
            sucesores = expandir(raiz)
            cerrados.add(raiz.estado)
            abiertos.extend(sucesores) #Si no es la solucion, expando y añado los nodos a la lista de abierto para mirarlo en la proxima interseccion
    # Completar
    if not objetivo:
        print("No se ha encontrado solución")
    if objetivo:
        dispSolucion(raiz)

# # Implementar la búsqueda en profundidad
def DFS() -> None:
    objetivo = False
    abiertos = []
    cerrados = set()
    sucesores = []
    # Inicializamos la pila con el estado inicial
    abiertos.append(NodoInicial())

    while abiertos and not objetivo:
        # Extraer el primer elemento (LIFO)
        actual = abiertos.pop(0)
        # Comprobamos si el estado actual es objetivo
        if testObjetivo(actual.estado):
            print("hola")
            objetivo = True
            dispSolucion(actual)
            break
        if actual.estado not in cerrados:
            cerrados.add(actual.estado)
            # Expandir sucesores del estado actual
            sucesores = expandir(actual)

            for s in reversed(sucesores):
            # Insertar sucesores al principio de la lista (pila)
            # pero evitando duplicados en abiertos y cerrados
            #prioridad a los nuevos
                abiertos.insert(0, s)


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
    cerrados = set()
    sucesores = []
    profundidad_actual = 0

    abiertos.append(NodoInicial())
    objetivo = False

    while abiertos and not objetivo:

        actual = abiertos.pop(0)
        cerrados.add(actual)

        
        objetivo = testObjetivo(actual.estado)

        if not objetivo and actual.profundidad < limite :

            sucesores = expandir(actual)
            
            if(buscarRepetidos2(actual, cerrados)):
                #si el nuevo sucesor no es el mismo que hemos tenido en cerrado lo añadimos
                #una vez comprobado que no está en cerados debemos de comprobar si es igual en abiertos 
                if(buscarRepetidos1(actual, abiertos)):
                    abiertos = sucesores + abiertos
                    profundidad_actual = 1;
    if not objetivo:
        print("No se ha encontrado solución")
    if objetivo:
        dispSolucion(actual)        

#     2. Búsqueda en Profundidad Limitada Iterativa.
    
def DLSI(limite_inicial: int):
    limite = limite_inicial
    while True:
        print(f"Probando con límite de profundidad: {limite}")
        if DLS(limite):
            print("Objetivo encontrado")
            return True
        limite += 1  # Incrementar límite y volver a intentar


def Voraz() -> None:
    abiertos = []
    cerrados = set()
    Sucesores = []  
    objetivo = False
    hash_abiertos = set()

    abiertos.append(NodoInicial())
    hash_abiertos.add(NodoInicial().estado.hash())


    while len(abiertos)> 0 and not objetivo :
        actual = abiertos.pop(0)
        hash_abiertos.discard(actual.estado.hash())

        objetivo = testObjetivo(actual.estado)

        if not objetivo : # si no es verdadero  
            repe = actual.estado.hash() in cerrados
            if not repe:        
                Sucesores = expandir(actual)
                #Ahora debemos de meter a los nodos sucesores de manera creciente en función de su heurística
                #Comprobamos que los sucesores no se repite en la lista de abiertos
                for s in Sucesores:
                    h = s.estado.hash()
                    if h not in cerrados and h not in hash_abiertos:
                        abiertos.append(s)
                        hash_abiertos.add(h)

                abiertos.sort()
                cerrados.add(actual.estado.hash())
                print(actual.heuristica)
            
    if not objetivo:
        print("No se ha encontrado solución")
    if objetivo:
        dispSolucion(actual)

#hay una opcion mas comoda
            # sorted(abiertos)
# def __it__(self, otro):
#             return self.heu < otro.heu, con A* self.heu + otro.costecamino < otro.heu < otro.costecamino
#   Podemos usar diccionario 


def Estrella() -> None:
    abiertos = {}
    cerrados = set()
    Sucesores = []
    objetivo = False

    abiertos.append(NodoInicial())
    while len(abiertos) > 0 and not objetivo:
        actual = abiertos.pop(0)
        objetivo = testObjetivo(actual.estado)

        if not objetivo : # si no es verdadero  
            repe = actual.estado.hash() in cerrados

            if not repe:
                Sucesores = expandir(actual)
                #Ahora debemos de meter a los nodos sucesores de manera creciente en función de su heurística
                # abiertos = abiertos + Sucesores
                abiertos.sort()
                cerrados.add(actual.estado.hash())

    if not objetivo:
        print("No se ha encontrado solución")
    if objetivo:
        dispSolucion(actual)