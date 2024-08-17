

#Problema2
'''''
num = int(input('ingrese un número: '))

if num % 2 == 0:
    print(f'el numero {num} es par')
else:
    print(f'el numero {num} es impar')
'''''

#Problema3
#sumatoria de los 100 primeros numeros naturales

"""""
num = 1
cont = 0

while num <= 100:

    cont += num
    num += 1

print(f'la sumatoria de los primeros 100 numeros naturales es {cont}')
"""""

#Problema4

password = 'pizza'

contra = input('Ingrese su contraseña: ')

while contra != password:
    print('Contraseña incorrecta. Vuelva a ingresarla')

print('Exito')
