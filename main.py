import xml.etree.ElementTree as ET
from xml.dom import minidom
import tkinter as tk
from tkinter import filedialog
from Listas.ListaC import ListaC
from Listas.Matrices import Matrices
import os
from graphviz import Digraph

def Menu():
    opcion = 0
    print(' ------------- Menu Principal -------------')
    print('1. Cargar Archivo')
    print('2. Procesar Archivo')
    print('3. Escribir Archivo de Salida')
    print('4. Datos del Estudiante')
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
            
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            
        return ruta

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
            listac = ListaC()
            for a in range(1, filas_n+1):
                listaf = ListaC()
                for b in range(1, columnas_m+1):
                    dato = matriz_xml.find(f"dato[@x='{a}'][@y='{b}']")
                    if dato is not None:
                        listaf.insertar(dato.text)
                    else:
                        listaf.insertar('0')
                
                listac.insertar(listaf, a)
        
            lista_t.insertar(listac, nombre_matriz)
            print(f"Matriz creada: {nombre_matriz} con {filas_n} filas y {columnas_m} columnas")
        return lista_t

    except ET.ParseError as pe:
        print(f"Error al procesar el archivo XML: {pe}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def merge(lista):
    if not lista.primero:
        return lista
    
    actualm = lista.primero
    while True:
        nombre = actualm.index
        listac = actualm.dato
        print(nombre)
        
        actualc = listac.primero
        
        while actualc:
            actual = actualc.siguiente
            while actual != listac.primero:
                if actualc.dato.binario() == actualc.dato.binario():
                    actualc.dato.mergeFila(actual.dato)
                    actualc.frecuencia += actual.frecuencia
                    
                    actual = fila(listac, actual)
                else:
                    actual = actual.siguiente

            actualc = actualc.siguiente
            if actualc == listac.primero:
                break
            
        actualm = actualm.siguiente
        if actualm == lista.primero:
            break
        
    return lista

def guardar(ruta_salida, tree):
    try:
        tree.write(ruta_salida, encoding='utf-8', xml_declaration=True)
        print(f"Archivo XML guardado exitosamente en {ruta_salida}")
    except Exception as e:
        print(f"Error al guardar el archivo XML: {e}")

def fila(lista, nodo):
    if nodo == lista.primero:
        return nodo.siguiente

    anterior = lista.primero
    while anterior.siguiente != nodo:
        anterior = anterior.siguiente

    anterior.siguiente = nodo.siguiente
    return anterior.siguiente

def abrirXML(lista, salida):
    root = ET.Element("matrices")

    actual_matriz = lista.primero
    while True:
        nombre_matriz = actual_matriz.index
        listac = actual_matriz.dato
        matriz_elem = ET.SubElement(root, "matriz", nombre=nombre_matriz, n=str(len(listac)), m=str(len(listac.primero.dato)), g=str(len(listac)))
        
        actualc = listac.primero
        x_index = 1  # Inicializar el índice x en 1
        while True:
            actualf = actualc.dato.primero
            count = 1
            while True:
                ET.SubElement(matriz_elem, "dato", x=str(x_index), y=str(count)).text = actualf.dato
                actualf = actualf.siguiente
                count += 1
                if actualf == actualc.dato.primero:
                    break

            actualc = actualc.siguiente
            x_index += 1
            if actualc == listac.primero:
                break
            
        actualc = listac.primero
        while True:
            ET.SubElement(matriz_elem, "frecuencia", g=str(actualc.index)).text = str(actualc.frecuencia)
            actualc = actualc.siguiente
            if actualc == listac.primero:
                break

        actual_matriz = actual_matriz.siguiente
        if actual_matriz == lista.primero:
            break

    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open(salida, "w") as f:
        f.write(xml_str)

def crear_ruta_salida(directorio, nombre_archivo):
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    ruta_salida = os.path.join(directorio, nombre_archivo)
    return ruta_salida

def generarGrafica(matriz, nombre_archivo):
    dot = Digraph(comment='Matriz Binaria')
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0

    for i in range(filas):
        for j in range(columnas):
            dot.node(f'{i},{j}', f'{matriz[i][j]}')

    for i in range(filas):
        for j in range(columnas - 1):
            dot.edge(f'{i},{j}', f'{i},{j+1}')

    for j in range(columnas):
        for i in range(filas - 1):
            dot.edge(f'{i},{j}', f'{i+1},{j}')

    dot.render(nombre_archivo, format='png')
    print(f"Gráfica generada exitosamente en {nombre_archivo}.png")


if __name__ == '__main__':
    lista = None
    ruta = ''
    lista_b = ListaC()
    lista_r = ListaC()
    opc = 0
    
    while opc != 6:
        opc = Menu()
        if opc == 1:
            root = tk.Tk()
            ruta = abrir_archivo()

        if opc == 2:
            if ruta:
                print()
                print('--------------------------------------------------')
                print('Procesando archivo...')
                print('--------------------------------------------------')
                print()
                lista = leerArchivoET(ruta)
                lista = merge(lista)                
            else:
                print("No hay datos para mostrar. Cargue el archivo primero.")
            print()
            
        if opc == 3:
            if lista:
                salida = input('Ingrese el nombre del archivo de salida: ')
                abrirXML(lista, salida)
                print(f"Archivo de salida guardado")
        if opc == 4:
            datosEstudiante()
            
        if opc == 5:
            nombre_archivo_grafica = input("Ingrese el nombre del archivo de salida para la gráfica (sin extensión): ")
            #generarGrafica(lista, nombre_archivo_grafica)
            #print('funcion no disponible...')
            
        if opc == 6:
            print(' --------------- Hasta luego --------------')
            print()
            print('       Gracias por utilizar el programa!')
            print()
            print()
            print()
            break
        
