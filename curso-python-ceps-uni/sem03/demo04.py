#Imprimir de 0 a 3
i = 0
while i < 4:
    print(i)
    i += 1
print('---------')
#Imprimir de 1 a 4
i = 0
while i < 4:
    i += 1
    print(i)
print('---------')
#Imprimir al reves
i = 4
while i > 0:
    i -= 1
    print(i)
print('---------')
i = 4
while i > 0: i -= 1; print(i)

print('---------')
i = 4
while i > 0: 
    i -= 1
    print(i)
else:
    print('El buble ha terminado')

print('-----Usando else and break----')
i = 4
while True: 
    i -= 1
    print(i)
    if i == 0:
        break;
else:
    print('El buble ha terminado')