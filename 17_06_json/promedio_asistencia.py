
import csv



lista_estudiantes = []
asistencia_final = 0
asistencia_estudiantes = []

with open('estudiantes.csv', 'r', newline= '', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    for i in datos:
        print(i)
        i[6] = asistencia_estudiantes
        lista_estudiantes.append(asistencia_estudiantes)
        print(asistencia_estudiantes)

     



        