lfrutas = ['manzana', 'platano', 'cereza', 'piña']
#anadir un elemento a la lista al final de la lista
lfrutas.append('uva')
print(lfrutas)
#anadir una lista a otra lista
lfrutas.extend(['pera', 'sandilla'])
print(lfrutas)
#insertar un elemento en el indice deseado
lfrutas.insert(1, 'naranja')
print(lfrutas)
#borrar el elemento indicado
lfrutas.remove('uva')
print(lfrutas)
#invertir el orden de la lista
lfrutas.reverse()
print(lfrutas)
#ordenar el elemento indicado
lfrutas.sort(reverse=True)
print(lfrutas)