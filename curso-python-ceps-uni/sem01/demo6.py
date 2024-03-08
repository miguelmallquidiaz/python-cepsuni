#Determinar si un número es positivo o negatico
from os import system
system('cls')
n = int(input('Ingrese número: '))

texto = ''

if (n >= 0):
    texto = 'El número es positivo'
else: 
    texto = 'El número es negativo'

print('\n-----------------------------------')
print('|            RESULTADO            |\n-----------------------------------')
print('|{:<10}|{:>22}|'.format("Respuesta", texto))
print('-----------------------------------')
