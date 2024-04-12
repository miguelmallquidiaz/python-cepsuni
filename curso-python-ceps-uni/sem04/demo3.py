num = int(input('Ingrese hasta que número imprimir: '))
x = 1
suma = 0
while x <= num:
    print(x)
    suma += x
    x += 1
print(suma)
print('')
for i in range(1, num + 1):
    print(i)