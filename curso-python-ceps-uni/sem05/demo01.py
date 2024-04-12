#Lista, tuplas, diccionarios para guardar varios datos
#               0       1           2       3
lfrutas = ['manzana', 'platano', 'cereza', 'piña']
#              -4       -3           -2       -1
lnumeros = [1, 2, 3]
print(lfrutas)
print(lnumeros)
#ver el tamaño con len
print(len(lfrutas))
#acceder al indice
print(lfrutas[0])
print(lfrutas[-1])
#Tipo de datos
print(type(lfrutas))
#imprimir lista utilizando for
for f in (lfrutas):
    print(f)
#modificar el segundo elemento
lfrutas[1] = 'papaya'
print(lfrutas)
#eliminar el cuarto elemento
del lfrutas[3]
print(lfrutas)
