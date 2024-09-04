from Listas_Binaria.listaC_Binaria import listaC_Binaria

class Matriz_Binaria:
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = listaC_Binaria()
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
        
    def imprimirListado(self):
        actual = self.datos.primero
        while True:
            print(f'({actual.dato[0]}, {actual.dato[1]}): {actual.dato[2]}', end=" -> ")
            actual = actual.siguiente
            if actual == self.datos.primero:
                break
        print()

    def comparar_filas(self):
        filas_dict = {}
        
        for dato in self.datos:
            if dato.x not in filas_dict:
                filas_dict[dato.x] = [0] * self.columnas
            filas_dict[dato.x][dato.y] = dato.dato

        filas_iguales = []
        for i in range(self.filas):
            for j in range(i + 1, self.filas):
                if filas_dict.get(i) == filas_dict.get(j):
                    filas_iguales.append((i, j))

        if filas_iguales:
            for (a, b) in filas_iguales:
                print(f"Fila {a + 1} es idéntica a Fila {b + 1}")
        else:
            print("No hay filas idénticas.")