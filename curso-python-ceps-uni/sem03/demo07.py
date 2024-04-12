#En una empresa trabajan n empleados cuyos sueldos oscilan entre 
#1000 y 5000. Realizar un programa que informe de cuantos empleados 
#cobran menos de 2000 y cuantos más de 2000. Informar también del total 
#que gasta la empresa en pagar a sus empleados
print('-'*40)
print('|         PAGO DE EMPLEADO             |')
print('-'*40)
cantidadEmpleado = int(input('Ingrese la cantidad de empleados: '))
print('-'*40)

i = 1
cobranMenos = 0
cobranMas = 0
total = 0
while i <= cantidadEmpleado:
    sueldo = float(input(f'Ingrese el sueldo del empleado {i}: '))
    if sueldo >= 1000 and sueldo <= 5000:
        if sueldo < 2000:
            cobranMenos += 1
        else:
            cobranMas += 1
    else:
        print("El sueldo debe estar entre 1000 a 5000")
    total += sueldo
    i += 1 # Contador siempre se va a sumar 1


print('-'*40)
print('Cantidad de empleados que ganan < 2000: ', cobranMenos)
print('Cantidad de empleados que ganan > 2000: ', cobranMas)
print('Total gastado en pagar a los empleados: ', total)
print('-'*40)
print('Creado por: Miguel Mallqui Diaz')
print('-'*40)