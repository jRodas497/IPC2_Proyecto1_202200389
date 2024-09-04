from Listas.Nodo import Nodo

class ListaC:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato)  # Creamos un nuevo nodo
        
#       filas, columnas, dato

        # Si la lista está vacía
        if self.primero is None:
            self.primero = nuevo
            self.primero.siguiente = self.primero
        # Si la lista no está vacía
        else:
            actual = self.primero  # Obtenemos el primero de la lista
            while actual.siguiente != self.primero:
                actual = actual.siguiente  # El nodo actual se mueve al siguiente
            actual.siguiente = nuevo  # Se agrega el nodo
            nuevo.siguiente = self.primero  # Hacemos que apunte al primero para cerrar el bucle/círculo
        self.size += 1

    def imprimir(self):
        if self.primero is None:
            print("La lista está vacía")
            return

        actual = self.primero
        while True:
            print(f"({actual.dato.x}, {actual.dato.y}): {actual.dato.dato}", end=" -> ")
            actual = actual.siguiente
            if actual == self.primero:
                break
        print()
        