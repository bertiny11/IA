#Misioneros y Canivales
from dataclasses import dataclass
import copy  

@dataclass
class tEstado:
    MisioneroDere :int
    MisioneroIzq :int
    CanibalDere: int
    CanibalIzq :int
    barco :bool     #si barco es 0 izq si 1 

    def __init__(self, MisioneroDere, MisioneroIzq, CanibalDere, CanibalIzq, barco):
        self.CanibalDere = CanibalDere
        #......

operadores = {1: "1Md", 2: "2Md", 3: "1M1Cd", 4: "1Cd", 5: "2Cd", 6: 
                "1Mi", 7: "2Mi", 8: "1M1Ci", 9: "1Ci", 10: "2Ci"}

def testObjetivo(estado :tEstado)-> bool: 
    #Que todos los Misioneros y Canibales han pasado la orilla
    objetivo = False
    if(estado.CanibalDere == 3 and estado.MisioneroDere == 3 and estado.barco == True):
        objetivo = True
    return objetivo


def esValido(estado :tEstado, op: int):
    valido = True
    if(estado.MisioneroDere <= estado.CanibalDere):
        valido = False
    if(estado.MisioneroIzq <= estado.CanibalIzq):
        valido = False
    if(estado.barco == True):
        if(op >= 1 and op <= 5):
            valido = False
    else:
        if(op >= 6 and op <= 10):
            valido = False
    # if(op >= 1 and op <= 5):
    #     if(estado.barco == True):
    #         valido = False
    # if(op >= 6 and op <= 10):
    #     if(estado.barco == False):
    #         valido = False
    return valido

def aplicaOperador(estado: tEstado, op : str):
    # nuevo = copy.deepcopy(estado)
    # #Debemos de tener en cuenta que la barca cambia de sitio y cambiar el numero de misioneros y canibales
    # match operadores[op]:
    #     case "1Md":
    pass
