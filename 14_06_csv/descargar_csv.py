import csv

lista_datos = []
lista_descarga = []

with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)

    for i in datos:
        lista_datos.append(i)

for fila in lista_datos:
    if fila[0] == 'nombre':
        lista_descarga.append(['nombre','asignatura', 'promedio', 'asistencia','estado'])
    else:
        promedio = float(fila[3]) + float(fila[4]) + float(fila[5])/ 3
        if promedio >= 4.0 and int(fila[6]) >= 60:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'
        nueva_fila = [fila[0], fila[2], promedio, fila[6], estado]
        lista_descarga.append(nueva_fila)



with open('descarga.csv', 'w', newline='') as descarga:
    descarga_reader = csv.writer(descarga)

    descarga_reader.writerows(lista_descarga)
