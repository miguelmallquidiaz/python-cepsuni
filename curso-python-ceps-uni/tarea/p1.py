#Ingresar 2 números enteros y luego intercambie sus valores
try:
    n1 = int(input("Ingresar el primer número: "))
    n2 = int(input("Ingresar el segundo número: "))

    print('---------------------------------')
    print('|     Números ingresados        |')
    print('---------------------------------')
    print('Primer número...........: ', n1)
    print('Segundo número..........: ', n2)

    print('\n---------------------------------')
    print('|     Números intercambiados     |')
    print('---------------------------------')
    print('Primer número...........: ', n2)
    print('Segundo número..........: ', n1)
    print('----------------------------------')
    print('Creado por: Miguel Mallqui Diaz')
    print('----------------------------------')
except:
    print("Ingrese correctamente los valores 🤨")