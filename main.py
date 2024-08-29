import xml.etree.ElementTree as ET # Importar librería ElementTree
from tkinter import filedialog
from Listas_Troncal.listaCircular_Troncal import lista_Troncal
from Listas_Troncal.matriz_Troncal import Matriz_Troncal
from Listas_Troncal.datos_Troncal import Datos_Troncal

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
    txt = ''
    
    ruta = filedialog.askopenfilename(filetypes=[('Archivo XML', '*.xml')])
    if ruta:
        with open(ruta, 'r', encoding='UTF-8') as file:
            txt = file.read()
    
    return txt

def leerArchivoET(rutaArchivo):
    tree = ET.parse(rutaArchivo)
    root = tree.getroot()
    
    for matriz_xml in root.findall('matriz'):
        nombre_matriz = matriz_xml.get('nombre')
        filas_n = int(matriz_xml.get('n'))
        columnas_m = int(matriz_xml.get('m'))
        
        if filas_n and columnas_m:
            datos_cantidad = (filas_n * columnas_m)
        
        matrizTroncal = Matriz_Troncal(filas_n, columnas_m, nombre_matriz, [])
        
        for dt in matriz_xml.findall('dato'):
            x = int(dt.get('x'))
            y = int(dt.get('y'))
            dato = int(dt.text.strip())
            
            datoTroncal = Datos_Troncal(x, y, dato)
            lista_Troncal.insertar(datoTroncal)
    
    lista_Troncal.imprimir()
            

if __name__ == '__main__':
    opc = 0
    
    while opc != 6:
        opc = Menu()
        if opc == 1:
            res = abrir_archivo()
            print(res)
            '''
            print(ruta)
        '''
        if opc == 2:
###         procesarArchivo()
            print()
            
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
        
