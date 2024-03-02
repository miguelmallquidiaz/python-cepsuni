#Determinar si un número es positivo o negatico

n = int(input('Ingrese número: '))

texto = ''

if (n >= 0):
    texto = 'El número es positivo'
else: 
    texto = 'El número es negativo' 

print('RESULTADOS\n--------------')
print('Respuesta...: ', texto)