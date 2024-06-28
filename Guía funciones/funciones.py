"""
1.- Crear función que según una palabra, me retorne su tamaño. No se puede ocupar len()
para este ejercicio.
2.- Crear función que me retorne un valor booleano en caso que el número sea Par.
3.- Crear una función que revisa una lista de números la cual será ingresada mediante input
por el usuario, debe obtener el promedio de esta lista según la cantidad de números que
existan en la lista.
4.- Crear una aplicación en donde pueda tener las siguientes opciones:
- Sumar números.
- Multiplicar números.
- Cantidad de números pares e impares.
- Obtener promedio de los números ingresados.
- Obtener la suma de los factoriales de cada número

"""

import lista_funciones

#1
word = input('Ingrese una palabra para ver su tamaño: ')
print('El tamaño de su palabra es:', lista_funciones.word_length(word))  

#2
num = int(input('Ingrese un número: '))
print(lista_funciones.parity(num))  

#3
number_list = []

num = float(input('Ingrese un número a la lista: '))
number_list.append(num)

while True:

    opcion = input('¿Quieres seguir añadiendo números? Responde (si) o (no): ')
    opcion = opcion.lower()
    if opcion == 'si':
        num = float(input('Ingrese un número a la lista: '))
        number_list.append(num)
        print(f'Números a promediar: {number_list}')
        
    elif opcion == 'no':
        print('El promedio final es: ', lista_funciones.number_average(number_list))
        break
    else:
        print('Ingresa una respuesta correcta ("si" / "no")')
        break



#Menu 

print('Bienvenide! \n ¿Cuál de las siguientes opciones quieres usar?: ')
print('1. Sumar números')
print('2. Multiplicar números')
print('3. Verificar números pares e impares')
print('4. Obtener un promedio de números')
print('5. Obtener la suma de los factoriales de cada número')
op_menu = int(input('Opción: '))




#while True:
#     numero = float(input("Ingrese un número : "))
#     lista_numeros.append(numero)
#     opcion = input("Desea agregar más numeros ? (si/no)").lower()
#     if opcion == "no":
#         break
#     elif opcion in ("s","si"):
#         continue
#     else:
#         print(f"Terminando pora aweonao")
#         break
# promedio_final = fn.promedio(lista_numeros)
# print(promedio_final)