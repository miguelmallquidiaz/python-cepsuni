a = 8
b = 5
c = a / b
print('La división de a=',a," y b=", b, " es ", c)
m = 9
n = 2
print('La división de m=',m," y n=", n, " es ", m/n)
x = 4
y = 0
# if y != 0:
try:
    m = 2 + 5
    m = 2 + 'Bye'
    # print('La división de x=',x," y y=", y, " es ", x/y)
except Exception as e:
    print('Se encontro una excepción ',e)
else:
    print(m)
    print('No ocurrió ninguna excepción')
finally:
    print(m)
    print('Este es el bloque de finally')

'''except TypeError:
    print('Tipos de datos diferentes')'''