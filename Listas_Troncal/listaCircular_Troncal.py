'''
-----    LISTA CIRCULAR TRONCAL    -----
'''

from .nodo_Troncal import Nodo_Troncal as Nodo

class lista_Troncal:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato) # Creamos un nuevo nodo

# Si la lista está vacía
        if self.primero == None: 
            self.primero = nuevo
            self.primero.siguiente = self.primero
# Si la lista no está vacía
        else: 
            actual = self.primero # Obtenemos el primero de la lista
            while actual.siguiente != self.primero:
                actual = actual.siguiente  # El nodo actual se mueve al siguiente
            actual.siguiente = nuevo # Se agrega el nodo
            nuevo.siguiente = self.primero # hacemos que apunte al primero para cerrar el bucle|círculo
        self.size += 1

    def imprimir(self):
        actual = self.primero
        for i in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            i += 1