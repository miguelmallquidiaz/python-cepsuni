# Leer cuatro números y determinar el número menor

try:
    print('-------------------------------------')
    print('|        INGRESAR NÚMEROS           |')
    print('-------------------------------------')
    
    n1 = int(input('Ingresar el primer número.....: '))
    n2 = int(input('Ingresar el segundo número....: ')) 
    n3 = int(input('Ingresar el tercer número.....: '))
    n4 = int(input('Ingresar el cuarto número.....: '))

    if n2 < n1:
        numMenor = n2
        texto = 'segundo'
    elif n3 < n2:
        numMenor = n3
        texto = 'tercero'
    elif n4 < n3:
        numMenor = n4
        texto = 'cuarto'
    else:
        numMenor = n1
        texto = 'primer'
    
    print('-------------------------------------')
    print('|            RESULTADO              |')
    print('-------------------------------------')
    print('El',texto, 'número es el menor y es', numMenor)
    print('-------------------------------------')
    print('Creado por: Miguel Mallqui Diaz')
    print('-------------------------------------')
except:
    print('Ingresar correctamente los valores 🤨')