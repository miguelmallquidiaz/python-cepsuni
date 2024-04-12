#Escribir un programa que solicite ingresar la nota de 8 alumnos, 
#el programa debe informar de cuantos han aprobado y cuantos han desaprobado.

print('---------------------------------')
print('|      INGRESO DE NOTAS         |')
print('---------------------------------')

i = 1
aprobado = 0
desaprobado = 0
while i <= 8:
    nota = int(input(f'Ingrese nota {i}: '))
    if nota >=12:
        aprobado += 1
    else:
        desaprobado +=1
    i += 1 # Contador siempre se va a sumar 1

print('----------------------------------')
print('La cantidad de aprobados es ...: ', aprobado)
print('La cantidad de desaprobados es.: ', desaprobado)
print('----------------------------------')
print('Creado por: Miguel Mallqui Diaz')
print('----------------------------------')