
def calculo_promedio(lista_alumnos):
    round((float(i[5]) + float(i[6]) + float(i[7])) / 3, 2)


def mejor_alumno_asignatura(lista_alumnos):
    asignaturas = []
    for i in lista_alumnos:
        print(i[5])
        for i in lista_alumnos:
            asignaturas.append(i['asignatura'])
            return asignaturas


