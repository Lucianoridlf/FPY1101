#promedio alto

import csv
lista_datos = []
lista_biologia = []

with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    lista_datos = csv.reader(archivo)

    promedio_alto = 0
  

    for i in lista_datos:
        asignatura = i[2]
        if i[2] == "Biología":
            lista_biologia.append(i)
        
    suma = 0
    promedio_alto = 0
    lista_promedios =[]

for j in lista_biologia:
    promedio_biologia = float(j[3]) + float(j[4]) + float(j[5])/ 3
    lista_promedios.append(promedio_biologia)

    if promedio_biologia > promedio_alto:
         promedio_alto = promedio_biologia
    print(promedio_alto)
    print(j[0], j[1])
    