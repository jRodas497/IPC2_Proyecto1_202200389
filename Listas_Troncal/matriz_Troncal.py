class Matriz_Troncal:
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = {}
        self.contador_datos = 0  # Contador para los datos insertados

    def insertar(self, x, y, dato):
        if self.contador_datos < self.filas * self.columnas:
            self.datos[(x, y)] = dato
            self.contador_datos += 1
        else:
            raise ValueError("No se pueden insertar más datos, la matriz ya está completa.")

    def imprimir(self):
        if self.contador_datos != self.filas * self.columnas:
            raise ValueError("La matriz no está completa. Faltan datos.")
        
        for i in range(self.filas):
            secuencia = []
            for j in range(self.columnas):
                if (i, j) in self.datos:
                    secuencia.append(str(self.datos[(i, j)]))
                else:
                    secuencia.append("0")  # Asumiendo que los valores no presentes son 0
            print(" -> ".join(secuencia))

        
# n = filas
# m = columnas