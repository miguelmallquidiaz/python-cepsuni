#Elabore un programa que calcule el promedio final de un curso, teniendo en cuenta lso siguientes pesos

pc1 = int(input('Práctica 1..........:'))
pc2 = int(input('Práctica 2..........:'))
ep = int(input('Examen Parcial......:'))
ef = int(input('Examen Final........:'))

promedio = (pc1 * 1 + pc2 * 2 + ep * 3 + ef * 3) / 9

print('\nEl promedio es: {:.2f}'.format(promedio))