tupla_numero = (2, 3, 4)
print(tupla_numero)

#No se puede modificar

#Pasar una lista a tupla
lista_numero = [1, 2 , 3, 2 ,2]
tnum = tuple(lista_numero)
print(type(tnum))

for n in tupla_numero:
    print(n)
for n in tnum:
    print(n)

#Contar la cantidad de veces el número
print('La cantidad es :', tnum.count(2))