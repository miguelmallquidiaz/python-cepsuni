from Empleado import Empleado
from Cliente import Cliente

nombre = apellido = dni = telefono = ""

def datos():
    nombre = input('Ingrese nombre: ')    
    apellido = input('Ingrese apellido: ')    
    dni = input('Ingrese DNI: ')    
    telefono = input('Ingrese telefono: ') 

def cargar():
    respuestaDeOpcion = input(
        """====== OPCIONES ======
        \nVas a agregar un empleado escriba 'e': 
        \nVas a agregar un cliente esciba 'c': 
        \nQuiere salir de la app escriba 'salir': 
        \nSelecione la opción: """
        )
    if respuestaDeOpcion.lower() == 'e':
        datos()
        salario = float(input('Ingresar salario: '))
        saliaroRedondeado = round(salario, 2)
        empleado = Empleado(nombre, apellido, dni, telefono, saliaroRedondeado)
        personas.append(empleado)
    elif respuestaDeOpcion.lower() == 'c':
        datos()
        categoria = input('Ingresar la categoria: ')
        cliente = Cliente(nombre, apellido, dni, telefono, categoria)
        personas.append(cliente)
    elif respuestaDeOpcion.lower() == 'salir':
        return
    else:
        print('Ingrese la opción correcta 🤨')

personas = []
cargar()
cargar()