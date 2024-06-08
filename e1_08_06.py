#Al menos debe tener 4 nombres con sus datos y estos debe ingresar por teclado
#Crear agenda telefónica donde la estructura diccionario debe ser la siguiente:
#
#       "nombre":{
#          "teléfono": string
#          "email":
#          "direccion": string
#          "estado": boolean
# }


lista_datos = []
cantidad_usuario = 2

for i in range (cantidad_usuario):
    datos_usuario = {}
    nombre = input("Ingrese su nombre: ")
    telefono = int(input("Ingrese su teléfono: "))
    email = input("Ingrese su email: ")
    direccion = input("Ingrese su dirección: ")
    estado = bool(input("Estado: "))
    

    datos_usuario[nombre] = {
            "teléfono": telefono,
            "email": email,
            "dirección": direccion,
            "estado": estado

    }
    lista_datos.append(datos_usuario)

print(lista_datos)
