#Ingrese 2 números, cálcule n2 muestre las operaciones básicas: +, - , producto
# / n2 resto entre ambos valores
n1 = int(input('Ingrese número 1: '))
n2 = int(input('Ingrese número 2: '))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2
resto = n1 % n2

print('========Operaciones básicas========')
print('----------------------------------')
print('La suma es: ', suma)
print('La resta es: ', resta)
print('El producto es: ', producto)
print('La división es: {:.2f}'.format(division))
print('El resto es: ', resto)
print('----------------------------------')