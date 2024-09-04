from Listas.ListaC import ListaC

class Matrices:
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = ListaC()
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
        
    def volver_binario(self):
        matriz_binaria = Matrices(self.filas, self.columnas, self.nombre + '_binaria')
        actual = self.datos.primero
        if actual:
            while True:
                x, y, valor = actual.dato
                dato_binario = 1 if valor > 0 else 0
                matriz_binaria.insertar(x, y, dato_binario)
                actual = actual.siguiente
                if actual == self.datos.primero:
                    break
        return matriz_binaria
    
    def trabajar_resultante(self, binarias):
        matriz_resultante = Matrices(self.filas, self.columnas, self.nombre + '_resultante')
        actual = self.datos.primero
        if actual:
            while True:
                x, y, valor = actual.dato
                dato_resultante = valor * 3
                matriz_resultante.insertar(x, y, dato_resultante)
                actual = actual.siguiente
                if actual == self.datos.primero:
                    break
        return matriz_resultante