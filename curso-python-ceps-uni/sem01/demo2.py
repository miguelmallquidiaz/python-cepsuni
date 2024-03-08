#Ingrese 2 números, cálcule n2 muestre las operaciones básicas: +, - , producto
# / n2 resto entre ambos valores
n1 = int(input('Ingrese número 1: '))
n2 = int(input('Ingrese número 2: '))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2
resto = n1 % n2
print('\n---------------------------------')
print('|      Operaciones básicas      |')
print('---------------------------------')
print('|{:<20}|{:>10.2f}|'.format('La suma es: ', suma))
print('|{:<20}|{:>10.2f}|'.format('La resta es: ', resta))
print('|{:<20}|{:>10.2f}|'.format('El producto es: ', producto))
print('|{:<20}|{:>10.2f}|'.format('La división es: ', division))
print('|{:<20}|{:>10.2f}|'.format('El residuo es: ', resto))
print('---------------------------------')