'''
a = 120
b = 50

if b > a:
    print('b es mayor que a')
elif a == b:
    print('a y b son iguales')
else:
    print('a es mmayor que b')
'''
# Ejercicio si el alumno tiene una nota a partir de 12 aprobado, a partir de 8 subsanación
# Caso contrario desaprobado, Qué el alumno ingrese su 3 notas y sacar el promedio
'''
print('---------------------------------')
print('|  Calcular Promedio de Notas   |')
print('---------------------------------')
n1 = float(input('Ingrese nota 1: '))
n2 = float(input('Ingrese nota 2: '))
n3 = float(input('Ingrese nota 3: '))
print('---------------------------------')
promedio = (n1 + n2 + n3) / 3

if promedio >= 12:
    print('El alumno esta Aprobado con: {:.2f}'.format(promedio))
elif promedio >= 8:
    print('El alumno va a Subsanación con: {:.2f}'.format(promedio))
else:
    print('El alumno esta Desaprobado con {:.2f}'.format(promedio))
print('---------------------------------')
print('Credo por: Miguel Mallqui')
print('---------------------------------')
'''

# Sacar las áreas 1. Del triangulo, 2 del circulo, 3 del cuadrado, 4 del rectangulo

op = int(input('''
1. Del triangulo
2 del circulo
3 del cuadrado
4 del rectangulo
Elige una opción: '''))
print('---------------------------------')
print('|        Calcular Área           |')
print('---------------------------------')

if op == 1:
    base = float(input("Ingrese la longitud: "))
    altura = float(input("Ingrese la altura: "))
    area = 0.5 * base * altura
    print('El área del Triangulo es: {:.2f}'.format(area))
elif op == 2:
    radio = float(input("Ingrese el radio: "))
    area = 3.14 * radio * 2
    print('El área del Circulo es: {:.2f}'.format(area))
elif op == 3:
    lado = float(input("Ingrese la longitud del lado: "))
    area = lado * 2
    print('El área del Cuadrado es: {:.2f}'.format(area))
else:
    base = float(input("Ingrese la longitud de la base:: "))
    altura = float(input("Ingrese la altura:: "))
    area = base * altura
    print('El área del Cuadrado es: {:.2f}'.format(area))
print('---------------------------------')
print('Credo por: Miguel Mallqui')
print('---------------------------------')
