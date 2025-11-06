from NPuzle_Alum import estadoInicial, aplicaOperador, testObjetivo, esValido, operadores
from Busqueda_Alum import DLS

estado = estadoInicial()
from time import time
inicio = time()
DLS(10)
fin = time()
print(fin-inicio)
# # Código para probar Npuzle - No requiere de la función de búsqueda
# while not testObjetivo(estado):
#     print(estado.t)
#     print("Introduzca el movimiento:")
#     print(operadores)
#     op = int(input(" "))
#     if esValido(op, estado):
#         estado = aplicaOperador(op, estado)
# if testObjetivo(estado):
#     print("Ha alcanzado el estado objetivo")

