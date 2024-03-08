arreglo = ['banana', 'melon', 'sandía', 'pera']

print('Mostar Las frutas que termianan con a: ')
for fruta in arreglo:
    #Determinar si la fruta termina con a
    if fruta.endswith('a'):
        print('La fruta es: ' + fruta)

arreglo.reverse()
print('\nMostar el arreglo al reves: ')
for fruta in arreglo:
    print('La fruta es: ' + fruta)

#Elimnar 
arreglo.remove('melon')
#Agregar
arreglo.append('kiwi')
print('\nMostar el arreglo al reves: ')
for fruta in arreglo:
    print('La fruta es: ' + fruta)

print('\nRecorrer número de 0 a 10: ')
for i in range(1, 10):
    print(i, end=" ")

