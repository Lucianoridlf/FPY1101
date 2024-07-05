import csv
import json
import funciones_csv as fn

def csv_a_json(archivo_csv):

    datos = []
    datos_json = []
    with open(archivo_csv, 'r', encoding='utf-8') as csvfile:
        datos_raw = csv.reader(csvfile)
        contador_filas = 0

        for i in datos_raw:
            if contador_filas == 0:
                contador_filas += 1
                continue
            else:
                datos.append(i)

        for i in datos:
            diccionario = {
                'rut' : i[0],
                'nombre' : i[1],
                'apellido' : i[2],
                'curso' : i[3],
                'asignatura' : i[4],
                'promedio' : round( (float(i[5]) + float(i[6]) + float(i[7])) / 3, 2),
                'asistencia' : i[8]
            }

            datos_json.append(diccionario)
    return datos_json

def obtener_categorias(datos, nombre_llave):
    datos = fn.csv_a_json('alumnos_detallado.csv')
    categorias = []

    for i in datos:
        categorias.append(i[nombre_llave])

    categorias = set(categorias)
    categorias = list(categorias)

    return categorias


def mejores_notas_asignaturas(datos):
    asignaturas = fn.obtener_categorias(datos,'asignatura')
    mejor_nota_asignatura = {}

    for i in asignaturas:
        mejor_nota_asignatura[i] = {
            'mejor_nota' : 0,
            'rut_alumno' : None
        }

    for i in datos:
        asignatura = i['asignatura']
        nota = i['promedio']
        rut = i['rut']

        for j in mejor_nota_asignatura.keys():
            if asignatura == j:
                if float(nota) > float(mejor_nota_asignatura[j]['mejor_nota']):
                    mejor_nota_asignatura[j]['mejor_nota'] = nota
                    mejor_nota_asignatura[j]['rut_alumno'] = rut

    with open('mejores_notas_asignatura.json', 'w', encoding='utf-8') as jsondump:
        json.dump(mejor_nota_asignatura,jsondump, indent=4)
    return mejor_nota_asignatura

def obtener_mejor_nota_anio(datos):
    cursos = fn.obtener_categorias(datos,'curso')

    mejores_notas_anio = {}

    for i in cursos:
        mejores_notas_anio[i] = {
            "mejor_nota" : 0,
            "rut_alumno" : None
        }
    

    ruts_unicos = fn.obtener_categorias(datos,'rut')

    promedios_rut = {}

    for i in ruts_unicos:
        promedios_rut[i] = 0

    for i in ruts_unicos:
        notas_alumno = []
        for j in datos:
            if i == j['rut']:
                nota = j['promedio']
                notas_alumno.append(nota)
        promedios_rut[i] = (sum(notas_alumno)/len(notas_alumno))

    for i in ruts_unicos:
        for j in datos:
            if i == j['rut']:
                anio = j['curso']
                promedio_final = promedios_rut[i]
                if float(promedio_final) > float(mejores_notas_anio[anio]['mejor_nota']):
                    mejores_notas_anio[anio]['mejor_nota'] = promedio_final
                    mejores_notas_anio[anio]['rut_alumno'] = i
                    
    with open('mejores_anios.json', 'w', encoding='utf-8') as jsondump:
        json.dump(mejores_notas_anio,jsondump, indent=4)
                    
    return  mejores_notas_anio

def obtener_mejor_asistencia_anio(datos):
    anio = fn.obtener_categorias(datos, 'curso')
    asignaturas = fn.obtener_categorias(datos,'asignatura')
    asistencias = fn.obtener_categorias(datos, 'asistencia')
    mejor_asistencia_asignatura = {}

    for i in anio:
        mejor_asistencia_asignatura[i] = {}
        for j in asignaturas:
            mejor_asistencia_asignatura[i][j] = 0
        
    # Obtener asistencia de cada asignatura

    for i in asignaturas:
        #print(f'Revisando {i}')
        lista_asistencia = []
        for j in datos:
            if i == j['asignatura']:
                asistencia_alumno = float(j['asistencia'])
                curso = j['curso']
                lista_asistencia.append(asistencia_alumno)
        promedio_asistencia = (sum(lista_asistencia) / len(lista_asistencia))
        mejor_asistencia_asignatura[curso][i] = promedio_asistencia
    

    for i in mejor_asistencia_asignatura:
        for j in asignaturas:
            if mejor_asistencia_asignatura[i][j] == 0:
                del mejor_asistencia_asignatura[i][j]
    print(mejor_asistencia_asignatura)
    
    #Obtener mejor asistencia de cada año

    for i in anio:
        asistencia_mayor = 0
        mejor_asignatura = ''
        print(f'Revisando {i}')
        llaves = list(mejor_asistencia_asignatura[i].keys())
        for j in llaves:
            if asistencia_mayor < float(mejor_asistencia_asignatura[i][j]):
                asistencia_mayor = float(mejor_asistencia_asignatura[i][j])
                mejor_asignatura = j

        print(f'La asistencia mayor es: {asistencia_mayor} \n Asignatura: {mejor_asignatura}')