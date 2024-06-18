
import json
import csv

lista_json = []

nombre_archivo = 'estudiantes_csv'
#abrir el archivo, w es escritura

try:
    with open(nombre_archivo, 'r', newline= '') as archivo:
        datos = csv.reader(archivo)
        for i in datos:
            datos_dict = {}
            datos_dict['notas'] = {}
            datos_dict['nombre'] = i[0]
            datos_dict['apellido'] = i[1]
            datos_dict['asignatura'] = i[2]
            datos_dict['notas']['nota1'] = i[3]
            datos_dict['notas']['nota2'] = i[4]
            datos_dict['notas']['nota3'] = i[5]
            datos_dict['asistencia_final'] = i[6]
            lista_json.append(datos_dict)

    for i in lista_json:
        print(i)

    with open('archivo.json', 'r') as archivo:
        datos_1 = json.dump(lista_json, archivo)

except FileNotFoundError:
    print('El archivo no existe')
except json.JSONDecodeError:
    print(f'Error en {datos}')
except Exception as e:
    print('Error', e)