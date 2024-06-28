import json
import csv

lista_alumnos = []

with open('alumnos_detallado.csv', 'r', newline= '', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)

    for i in datos:
        datos_dict = {}
        datos_dict['notas'] = {}
        datos_dict['rut'] = i[0]
        datos_dict['nombre'] = i[1]
        datos_dict['apellido'] = i[2]
        datos_dict['curso'] = i[3]
        datos_dict['asignatura'] = i[4]
        datos_dict['notas']['nota1'] = i[5]
        datos_dict['notas']['nota2'] = i[6]
        datos_dict['notas']['nota3'] = i[7]
        datos_dict['promedio'] = round((float(i[5]) + float(i[6]) + float(i[7])) / 3, 2)
        datos_dict['asistencia_final'] = i[8]
        lista_alumnos.append(datos_dict)

        if i[0] == 'rut':
            continue
        else:
        
        
        #Mejor alumno asignatura
            asignaturas = []
    
    for i in lista_alumnos:
        asignaturas.append(i['asignatura'])

        print(asignaturas)
    

    