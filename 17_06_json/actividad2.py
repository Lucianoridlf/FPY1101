import csv


with open('alumnos_detallado.csv', 'r', newline='', encoding='utf-8') as archivo:
    lista_datos = csv.reader(archivo)

    for i in lista_datos:
        print(i)
        dict_c
