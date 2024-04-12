#diccionario almacenar varios valoes clave: valor
diccionario = {
    'nombre' : 'Miguel',
    'Apellido': 'Mallqui',
    'Documento': ' 40561543'
}

print(diccionario)

for n in diccionario:
    print(n, diccionario[n])

#ELiminar el diccionario
#diccionario.clear()
diccionario.keys()
diccionario.values()

diccionario['Correo'] = 'cursos@gmail.com'
print(diccionario)

#Actualizar el diccionario
dnotas = {"nota1":13,"nota2":14, "edad": 30}
diccionario.update(dnotas)
print(diccionario)