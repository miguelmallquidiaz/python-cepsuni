# Ejercicio: Si se ingresa boleta que se muestre en la imagen y 
# si se ingresa factura   subtotal igv (18%) y total (monto a pagar)

tipo = input('¿Ingrese si es factura o boleta? ')

print('Datos de la Compra')
print('==================')

nomProd = input('Producto....: ')
cant = int(input('Cantidad....: '))
precio = float(input('Precio...S/:'))

if tipo == 'boleta':
    total = precio * cant

    print('RESULTADOS')
    print('------------\n')
    print('Producto..........: ', nomProd)
    print('Cantidad..........: ', cant)
    print('Precio..........S/:{:.2f} '.format(precio))
    print('Monto a pagar...S/:{:.2f} '.format(total))
if tipo == 'factura':
    subtotal = precio * cant
    subIgv = subtotal * 0.18
    total = subtotal * 1.18

    print('RESULTADOS')
    print('------------\n')
    print('Producto.............: ', nomProd)
    print('Cantidad.............: ', cant)
    print('precio.............S/: ', precio)
    print('Subtotal...........S/:{:.2f} '.format(subtotal))
    print('Subtotal IGV(18%)..S/:{:.2f} '.format(subIgv))
    print('Monto a pagar......S/:{:.2f} '.format(total))