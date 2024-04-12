#Realizar un programa que permita la carga de 5 valores por teclado 
#y posteriormente nos muestre la suma
print('---------------------------------')
print('|     INGRESO DE NÚMEROS        |')
print('---------------------------------')

i = 0
suma = 0
while i < 5:
    n = int(input('Ingreso el número: '))
    suma += n #Acumulador depende del valor que se ingrese
    i += 1 # Contador siempre se va a sumar 1

promedio = suma / i
print('----------------------------------')
print('La suma de los números es: ', suma)
print('El promedio es ..........: {:.2f}'.format(promedio))
print('----------------------------------')
print('Creado por: Miguel Mallqui Diaz')
print('----------------------------------')