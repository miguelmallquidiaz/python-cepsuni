#Ejemplo: Si ingresas un número y este 1000 ganastes un premio caso contrario sera para otra oportunidad
'''
print('---------------------------------')
print('|      LOTERIA PERÚ LOTO        |')
print('---------------------------------')

n = int(input('Ingrese un número: '))

if n == 1000 :
    print('ganastes un premio :)')
else:
    print('sera para otra oportunidad :(')

print('---------------------------------')
'''

#Ejemplo si los ventas fueron buenas el sueldo se incrementa en 30% caso contrario solo 5%
print('---------------------------------')
print('|      EMPRESA ROBLES S.A       |')
print('---------------------------------')

venta = input('¿Las ventas fueron buenas?: ')
sueldo = float(input('Ingresar su sueldo: '))

if venta == 'si' :
    sueldo += sueldo * 0.30
    print('\nEl sueldo se incrementa en 30%')
    print('El sueldo es: {:.2f}'.format(sueldo))
else:
    print('\nEl sueldo se incrementa en 5%')
    sueldo += sueldo * 0.05
    print('El sueldo es: {:.2f}'.format(sueldo))

print('---------------------------------')