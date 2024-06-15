import  csv

with open('estudiantes.csv', 'w', newline='') as archivo:
    escribir_csv = csv.writer(archivo)


    lista_datos = [
        ['Nombre', 'Apellido', 'Nota_1', 'Nota_2', 'Nota_3', 'Asistencia'],
        ['Juan', 'Perez', '6.0', '4.0', '2.5', '90']

    ]

    escribir_csv.writerow(lista_datos)