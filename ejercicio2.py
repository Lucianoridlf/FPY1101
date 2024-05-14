#2.- Contador de vocales y consonantes: 
#Solicita al usuario una cadena de texto y cuenta cuántas vocales y consonantes hay en ella.
#PISTA: 
#1.- usar if vocal in "aeiou", ejemplo if vocal in "aeiou" (Esto quiere decir que si la vocal esta dentro de la lista aeiou la condicion es True)
#2.- usar funcion .isalpha(), ejemplo if texto.isalpha(): (Esto quiere decir que si el texto contiene solo letras desde a-z es True)




vowel = 0
consonant = 0

while True:

    text = input('Ingrese una cadena de texto y cuenta cuantas vocales y consonantes: ')

    if text.isalpha():
        try:
            if text in 'aeiou':
                vowel += 1
            else:
                consonant += 1
        except ValueError:
            print('Error: Debes ingresar letras solamente')
    else:
        break

print('Cantidad de vocales: ', vowel)
print('Cantidad de consonantes: ', consonant)