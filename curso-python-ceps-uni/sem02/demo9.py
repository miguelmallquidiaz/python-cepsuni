# Ejercicio si la edad es desde 18 o su puntaje es > 100 muestra un
# mensaje en competencia caso contrario no puede competir

print('---------------------------------')
print('|     Registro de competencia   |')
print('---------------------------------')
edad = int(input('Ingrese edad: '))
puntaje = int(input('Ingrese puntaje: '))
print('---------------------------------')
if edad >= 18 or puntaje > 100:
    print('Puedes competir :)')
else:
    print('No puedes competir :(')
print('---------------------------------')
print('Realizado por: Miguel Mallqui')
print('---------------------------------')



