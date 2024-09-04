from listaCircular_Troncal import lista_Troncal

class Matriz_Troncal:
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = lista_Troncal()
        self.contador_datos = 0 

    def insertar(self, x, y, dato):
        if self.contador_datos < self.filas * self.columnas:
            self.datos.insertar((x, y, dato))
            self.contador_datos += 1
        else:
            raise ValueError("No se pueden insertar más datos, la matriz ya está completa.")

    def imprimir(self):        
        print(f'Nombre: {self.nombre} | {self.filas} x {self.columnas}')
        mtz = [['0' for _ in range(self.columnas)] for _ in range(self.filas)]
        actual = self.datos.primero
        if actual:
            while True:
                n, m, valor = actual.dato
                mtz[n-1][m-1] = str(valor)
                actual = actual.siguiente
                if actual == self.datos.primero:
                    break
        
        for fila in mtz:
            print(" -> ".join(fila))
        print('\n')
            
'''        for i in range(self.filas):
            secuencia = []
            for j in range(self.columnas):
                if (i, j) in self.datos:
                    secuencia.append(str(self.datos[(i, j)]))
                else:
                    secuencia.append("0")  # Asumiendo que los valores no presentes son 0
            print(" -> ".join(secuencia))'''

        
# n = filas
# m = columnas