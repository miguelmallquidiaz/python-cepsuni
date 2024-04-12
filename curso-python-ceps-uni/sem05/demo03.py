'''
Ejercicio 1 
Escribir un programa que almacene los cursos por ejemplo Matematicas, Física, Química, Historia y Lengua en una lista y la muestre por pantalla. Unos 6 cursos.
'''
course = ['Matematicas', 'Física', 'Química', 'Historia', 'Lengua', 'Programación']
print('----Cursos Asignados----')
for c in course:
    print(c)

'''
Ejercicio 2 
Del ejercicio anterior poner: En mi carrera profesional llevo el curso de <cursos>.
'''
print('----Cursos Qué llevo----')
for c in course:
    print(f'En mi carrera profesional llevo el curso de {c}')

'''
Ejercicio 3 
Se debe realizar 2 for, pregunte al usuario la nota que ha sacado en cada curso y despues mostrar en pantalla
'''
print('----Notas de Cursos----')
nota = 0
lista_nota = []
for c in course:
    nota = int(input(f'¿Cual es la nota del curso {c} ? '))
    lista_nota.append(nota)

#mostrat
for c in range(len(course)):
    print(f'En {course[c]} has sacado {lista_nota[c]}')

'''
Ejercicio 4 
Escribir un programa que almacene en una lista los siguientes precios 42, 75, 55, 38, 59, 62 , 54 y muestre por pantalla
'''
print('----Almacenar precios----')
lista_precio = [42, 75, 55, 38, 59, 62 , 54]
for p in lista_precio:
    print(p)

# lista si se puede cambiar sus valores []
#tuplas sus valores son constantes no se pueden cambiar ()
#diccionario {}