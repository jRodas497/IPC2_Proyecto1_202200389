import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from Listas.ListaC import ListaC
from Listas.Matrices import Matrices

def Menu():
    opcion = 0
    print(' ------------- Menu Principal -------------')
    print('1. Cargar Archivo')
    print('2. Listado de Matrices')
    print('3. Procesar Archivo a Binario')
    print('4. Lista de Matrices Binarias')
    print('5. Escribir Archivo de Salida')
    print('6. Lista de matrices de Salida')
    print('7. Mostrar Datos de Estudiante')
    print('8. Generar Gráfica')
    print('9. Salir')
    print(' ------------------------------------------')
    print('')


    opcion = int(input(' Ingrese su opción: '))
    print()

    return opcion

def datosEstudiante():

    print(' ------------------------------------------')
    print(" #######    DATOS DEL ESTUDIANTE    #######")
    print(' ------------------------------------------')
    print("-> JUAN JOSÉ RODAS MANSILLA               |")
    print("-> 202200389                              |")
    print("-> IPC2 Sección N                         |")
    print("-> Ingenieria en Ciencias y Sistemas      |")
    print('')

def abrir_archivo():
    print("Abriendo el cuadro de diálogo para seleccionar un archivo...")
    ruta = filedialog.askopenfilename(filetypes=[("Archivo XML", "*.xml")])
    if ruta:
        print(f"Archivo seleccionado: {ruta}")
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                txt = file.read()
                print("Contenido del archivo:")
                print()
                print("--------------------------------------------------")
                print(txt)
                print("--------------------------------------------------")
                print()
            
            return leerArchivoET(ruta)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

def leerArchivoET(rutaArchivo):
    try:
        tree = ET.parse(rutaArchivo)
        root = tree.getroot()
        
        lista_t = ListaC()
    
        for matriz_xml in root:
            nombre_matriz = matriz_xml.attrib['nombre']
            filas_n = int(matriz_xml.attrib['n'])
            columnas_m = int(matriz_xml.attrib['m'])
            
            matrizTroncal = Matrices(filas_n, columnas_m, nombre_matriz)
            
            for dt in matriz_xml:
                x = int(dt.attrib['x'])
                y = int(dt.attrib['y'])
                dato = int(dt.text)
                
                matrizTroncal.insertar(x, y, dato)
        

            lista_t.insertar(matrizTroncal)
            print(f"Matriz creada: {nombre_matriz} con {filas_n} filas y {columnas_m} columnas")
        return lista_t

    except ET.ParseError as pe:
        print(f"Error al procesar el archivo XML: {pe}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == '__main__':
    lista = None
    lista_b = ListaC()
    lista_r = ListaC()
    opc = 0
    
    while opc != 8:
        opc = Menu()
        if opc == 1:
            root = tk.Tk()
            lista = abrir_archivo()

        if opc == 2:
            if lista:
                actual = lista.primero
                if actual:
                    while True:
                        actual.dato.imprimir()
                        actual = actual.siguiente
                        if actual == lista.primero:
                            break
            else:
                print("No hay datos para mostrar. Cargue el archivo primero.")
            print()
            
        if opc == 3:
            if lista:
                print('Procesando archivo...')
                print()
                actual = lista.primero
                if actual:
                    while True:
                        matriz_01 = actual.dato.volver_binario()
                        print(f'Matriz binaria generada: {matriz_01.nombre}')
                        lista_b.insertar(matriz_01)
                        actual = actual.siguiente
                        if actual == lista.primero:
                            break
                    print()
                    print('Listado de matrices binarias generadas.')
            else:
                print("No se encuentra ninguna matriz existente.")
            
            print()
            
        if opc == 4:
            if lista_b.primero:
                actual = lista_b.primero
                if actual:
                    while True:
                        actual.dato.imprimir()
                        actual = actual.siguiente
                        if actual == lista_b.primero:
                            break
            else:
                print("Aún no se han generado matrices binarias.")
            
        if opc == 5:
###         generarGrafica()
            print()
            
        if opc == 6:
            datosEstudiante()
            break
        
        if opc == 7:
            print('Función pendiente de implementar')
        
        if opc == 8:
            print('Función pendiente de implementar')
        
        if opc == 8:
            print(' --------------- Hasta luego --------------')
            print()
            print('       Gracias por utilizar el programa!')
            print()
            print()
            print()
            break
        
        print()
        
