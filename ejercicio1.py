#1.- Contador de números pares e impares: 
#Escribe un programa que cuente y muestre cuántos números pares e impares 
#hay en una lista de números ingresada por el usuario.

par=0
impar=0

while True:
    
    try:
        num = int(input('Ingrese un número: '))

        if num == 0:
            break

        if num % 2 == 0:
            par += 1

        else:
            impar += 1

    except ValueError:
        print('Ingrese un número solamente')

#Cantidad de pares e impares

print('Cantidad de números pares: ', par)
print('Cantidad de números impares: ', impar)
