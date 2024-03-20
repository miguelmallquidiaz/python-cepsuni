from os import system
system('cls')

def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascci = ord(letra)
        ascci += 1
        textoFinal += chr(ascci)
    # print('El texto encriptado es: ' +textoFinal)
    return textoFinal

def desencriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascci = ord(letra)
        ascci -= 1
        textoFinal += chr(ascci)
    # print('El texto a desencriptado es: ' +textoFinal)
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo se encripto correctamente 🙊')

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()

    print('El archivo se desencripto correctamente 🙉')

respuestaOpciones = input(
    'Opciones: \nPresionar E o e para encriptar\nPresionar D o d para desencriptar\nElige la opción: '
    )
def obtenerRuta():
    rutaArchivo = input('Ingresar la ruta del archivo: ')
    return rutaArchivo

match respuestaOpciones:
    case 'E': 
        encriptarArchivo(obtenerRuta())
    case 'e':
        encriptarArchivo(obtenerRuta())
    case 'D':
        desencriptarArchivo(obtenerRuta())
    case 'd':
        desencriptarArchivo(obtenerRuta())
    case _:
        print('Elegir una opción valida 🤨')

