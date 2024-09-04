from datos_Binaria import Datos_Binaria

class Matriz_Binaria:
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.datos = []

    def insertar(self, x, y, dato):
        self.datos.append(Datos_Binaria(x, y, dato))

    def imprimir(self):
        matriz = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
        for dato in self.datos:
            matriz[dato.x][dato.y] = dato.dato

        for fila in matriz:
            print(" -> ".join(map(str, fila)))

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
'''
    def guardar(self, ruta):
        with open(ruta, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def cargar(ruta):
        with open(ruta, 'rb') as file:
            return pickle.load(file)'''