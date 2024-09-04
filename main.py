import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from Listas_Troncal.listaCircular_Troncal import *
from Listas_Troncal.matriz_Troncal import *
from Listas_Troncal.datos_Troncal import *
from Listas_Binaria.matriz_Binaria import *


def Menu():
    opcion = 0
    print(' ------------- Menu Principal -------------')
    print('1. Cargar Archivo')
    print('2. Procesar Archivo')
    print('3. Escribir Archivo de Salida')
    print('4. Mostrar Datos de Estudiante')
    print('5. Generar Gráfica')
    print('6. Salir')
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
            
            leerArchivoET(ruta)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

def leerArchivoET(rutaArchivo):
    try:
        tree = ET.parse(rutaArchivo)
        root = tree.getroot()
        
        lista_t = lista_Troncal()
    
        for matriz_xml in root:
            nombre_matriz = matriz_xml.attrib['nombre']
            filas_n = int(matriz_xml.attrib['n'])
            columnas_m = int(matriz_xml.attrib['m'])
            
            if filas_n and columnas_m:
                datos_cantidad = (filas_n * columnas_m)
            
            matrizTroncal = Matriz_Troncal(filas_n, columnas_m, nombre_matriz)
            print(f"Matriz creada: {nombre_matriz} con {filas_n} filas y {columnas_m} columnas")
            
            for dt in matriz_xml:
                x = int(dt.attrib['x'])
                y = int(dt.attrib['y'])
                dato = int(dt.text)
                
                datoTroncal = Datos_Troncal(x, y, dato)
                lista_t.insertar(datoTroncal)
                matrizTroncal.insertar(x, y, dato)
        
        lista_t.imprimir()
        matrizTroncal.imprimir()
        
        ###BIN
        nombre_binario = nombre_matriz + '_bin'
        matrizBinaria = Matriz_Binaria(filas_n, columnas_m, nombre_binario)
        for dt in matriz_xml.findall('dato'):
            x = int(dt.get('x'))
            y = int(dt.get('y'))
            dato = int(dt.text.strip())
            matrizBinaria.insertar(x, y, 1 if dato > 0 else 0)
        
        matriz_binaria_global = matrizBinaria
        print(f"Matriz binaria creada: {nombre_binario}")
        
        if matrizTroncal.contador_datos != datos_cantidad:
            print(f"Advertencia: Se esperaban {datos_cantidad} datos, pero se insertaron {matrizTroncal.contador_datos}.")

    except ET.ParseError as pe:
        print(f"Error al procesar el archivo XML: {pe}")
    except Exception as e:
        print(f"Error inesperado: {e}")
            
def procesar_archivo():
    global matriz_binaria_global
    if matriz_binaria_global:
        matriz_binaria_global.imprimir()
        matriz_binaria_global.comparar_filas()
    else:
        print("No hay registros anteriores. Por favor, cargue un archivo primero.")


if __name__ == '__main__':
    opc = 0
    
    while opc != 6:
        opc = Menu()
        if opc == 1:
            root = tk.Tk()
            abrir_archivo()

        if opc == 2:
            procesar_archivo()
            
        if opc == 3:
###         escribirArchivoSalida()
            print()
            
        if opc == 4:
            datosEstudiante()
            print()
            
        if opc == 5:
###         generarGrafica()
            print()
            
        if opc == 6:
            print('Hasta luego!')
            break
        
        print()
        
