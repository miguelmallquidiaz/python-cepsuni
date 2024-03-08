#Alinear textos en python con format alinea a la izquierda o derecha de una determinanda cantidad de espacios en blanco

# Los espacios en python o tabulaciones se le conoce como sangría o identación 

# Alinear a la izquierda
nombre = "luis"
# En el argumento que estan las llaves el total de caracteres y lo demás lo ponga reemplaze con espacios sobrantes.
print('Alineación a la izquierda')
print('|{:<20}|'.format(nombre))

#Alinear a la derecha: Pone todo el caracter a la derecha y rellenar con espacios en blanco
nombre = "Ana"
print('Alineación a la derecha')
print('|{:>20}|'.format(nombre))

#Ejemplo con tablas
datos = [
    {
        "nombre":"Luis",
        "promedio":9.5,
    },
    {
        "nombre":"Jhon",
        "promedio":8.96,
    },
    {
        "nombre":"Leo",
        "promedio":9.22,
    }
]
print('\n---------------------------------')
print('|{:<20}|{:>10}|'.format("Nombre","Promedio"))
print('---------------------------------')
for dato in datos:
    nomre = dato['nombre']
    promedio = dato['promedio']
    cadena = '|{:<20}|{:>10.2f}|'.format(nombre, promedio)
    print(cadena)
    print('---------------------------------')