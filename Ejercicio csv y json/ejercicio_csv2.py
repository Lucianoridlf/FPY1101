import csv
import json
import funciones_csv as fn

# Datos principales
datos = fn.csv_a_json('alumnos_detallado.csv')

# Ciclo para Menú 
while True:
    print('Bienvenido(a), Ingrese la opción que desea:')
    print('-------------------------------------------')
    print('1.- Obtener el mejor alumno por asignatura')
    print('2.- Obtener el mejor alumno por año')
    print('3.- Obtener la asignatura de cada año con la mejor asistencia')
    print('4.- Salir')
    print('-------------------------------------------')
    opcion_menu = int(input('Opción número: '))
    

    # Mejor nota por asignatura
    if opcion_menu == 1:
        mejores_notas_asignatura = fn.mejores_notas_asignaturas(datos)
        print('Buscando alumno con mejor nota por asignatura...')
        print(mejores_notas_asignatura)


     # Mejor alumno por año
    elif opcion_menu == 2:
        mejores_alumnos_anio = fn.obtener_mejor_nota_anio(datos)
        print('Agrupando mejores alumnos por año...')
        print(mejores_alumnos_anio)


    # Mejor nota por año
    elif opcion_menu == 3:
        mejor_asistencia_por_anio = fn.obtener_mejor_asistencia_anio(datos)
        print('Revisando asistencia de asignatura por cada año...')
        print(mejor_asistencia_por_anio)

    # Salir del Menu
    elif opcion_menu == 4:
        print('Saliendo de menú...')
        print('¡Adiós!')
        break

    else:
        print('Escoja una opción válida')
        

