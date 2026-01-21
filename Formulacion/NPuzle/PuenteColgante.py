from dataclasses import dataclass
import copy

operadores = [
    (0,), (1,), (2,), (3,),          # Movimientos individuales
    (0, 1), (0, 2), (0, 3),          # P1 con alguien
    (1, 2), (1, 3),                  # P2 con alguien
    (2, 3)                           # P3 con P4
]#la logica que voy a usar es la siguiente: el que mas tarde va a ir acompañado siempre del que tarde menos en ir, asumiremos que p1 esta en la posicion de la lista de 0

@dataclass
class tEstado:
    izquierda: list #sera una lista de 4 elementos inicialmente, cada elemnto sera el tiempo que dura cada persona en cruzar
    linterna: int #la linterna tendra el valor de 0 o 1 dependiendo de donde este
    derecha: list #lista donde se encuentren las personas cruzadas

    def __init__(self, izquierda, linterna, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
        self.linterna = linterna

def esValido(estado: tEstado, op: tuple) -> bool:
    # Determinamos en qué orilla está la linterna para saber dónde buscar
    # 0 = Izquierda, 1 = Derecha
    lista_origen = estado.izquierda if estado.linterna == 0 else estado.derecha
    
    # Comprobamos si TODAS las personas del operador están en esa orilla
    for persona in op:
        if persona not in lista_origen:
            return False # Si falta alguien, el movimiento no es válido
            
    return True

def aplicaOperador(estado: tEstado, op: tuple) -> tEstado:
    # 1. Creamos una copia profunda para no modificar el estado anterior
    nuevo = copy.deepcopy(estado)
    
    # 2. Lógica de movimiento
    if estado.linterna == 0: # Mover de Izquierda -> Derecha
        for persona in op:
            nuevo.izquierda.remove(persona) # Sacamos de origen
            nuevo.derecha.append(persona)   # Metemos en destino
        nuevo.linterna = 1 # La linterna cruza
        
    else: # Mover de Derecha -> Izquierda
        for persona in op:
            nuevo.derecha.remove(persona)
            nuevo.izquierda.append(persona)
        nuevo.linterna = 0 # La linterna vuelve

    # (Opcional) Ordenar listas ayuda a ver mejor el estado al imprimirlo
    nuevo.izquierda.sort()
    nuevo.derecha.sort()
    
    return nuevo

def heuristica(estado: tEstado) -> int:
    # Si ya no queda nadie en la izquierda, el coste estimado es 0
    if not estado.izquierda:
        return 0
    
    # Heurística Admisible: El tiempo del más lento que queda en la izquierda.
    # Es optimista porque asume que los demás cruzan "gratis" con él.
    return max(estado.izquierda)

#def Estrella():
    