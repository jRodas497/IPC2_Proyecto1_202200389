from Listas.Nodo import Nodo

class ListaC:
    def __init__(self):
        self.primero = None
        self.size = 0
        
    def __len__(self):
        if not self.primero:
            return 0
        actual = self.primero
        count = 1
        while actual.siguiente != self.primero:
            count += 1
            actual = actual.siguiente
        return count

    def insertar(self, dato, index = None):
        nuevo = Nodo(dato, index)  # Creamos un nuevo nodo
        
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
            print(f"({actual.dato}, {actual.dato.y}): {actual.dato.dato}", end=" -> ")
            actual = actual.siguiente
            if actual == self.primero:
                break
        print()
        
    def binario(self):
        patron = ''
        actual = self.primero
        while True:
            patron += "1" if int(actual.dato) > 0 else "0"
            actual = actual.siguiente
            if actual == self.primero:
                break
        return patron
    
    def mergeFila(self, fila):
        actual = self.primero
        actualf = fila.primero
        while True:
            actual.dato = str(int(actual.dato) + int(actualf.dato))
            actual = actual.siguiente
            actualf = actualf.siguiente
            if actual == self.primero or actualf == fila.primero:
                break
        return self
        