try:
    print('----------------------------------------------')
    print('|            VIAJE POR CRUCERO               |')
    print('----------------------------------------------')
    precioDelCrucero = float(input('Ingrese el precio del crucero: S/.'))
    diasDeAnticipacion = int(input('Ingrese la cantidad de días de anticipación: '))
    edad = int(input('Ingrese su edad: '))
    realizoOtroCrucero = input('¿Ha tomado otro crucero antes (Si/No)?: ').upper()

    if diasDeAnticipacion >= 17:
        if 28 <= edad <=30:
            descuento = 0.115
        else:
            descuento = 0.078
    elif diasDeAnticipacion >= 9 and realizoOtroCrucero == "SI":
        descuento = 0.02
    else:
        descuento = 0

    precioConDescuento = precioDelCrucero * descuento

    precioTotal =  precioDelCrucero - precioConDescuento

    print('----------------------------------------------')
    print('|            RESULTADO                       |')
    print('----------------------------------------------')
    print('El Descuento aplicado es......: ', descuento * 100, "%")
    if descuento != 0:
        print('El Precio con descuento es....: S/.{:.2f}'.format(precioConDescuento))
        print('El precio total es............: S/.{:.2f}'.format(precioTotal))
    else:
        print('El precio total es............: S/.{:.2f}'.format(precioTotal))
    print('----------------------------------------------')
    print('Creado por: Miguel Mallqui Diaz')
    print('----------------------------------------------')
except:
    print('Ingresar correctamente los valores 🤨')