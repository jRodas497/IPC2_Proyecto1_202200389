import xml.etree.ElementTree as ET # Importar librería ElementTree

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

    try:
        opcion = int(input(' Ingrese su opción:'))
        print()
    except ValueError:
        print("Error: Debes ingresar un número entero.")

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

if __name__ == '__main__':
    opc = 0
    
    while opc != 6:
        opc = Menu()
        if opc == 1:
###         cargarArchivo()
            print()
        
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
        
