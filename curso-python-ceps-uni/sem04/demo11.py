'''Nuestro sistema ha sufrido un daño en la base de datos debido a que un formulario no esta funcionando correctamente,
por lo tanto han llegado emails corruptos. Corregir el email como consideres para que sea útil y poder enviarles
las novedades y avisos a los clientes acerca de nuestro negocio:'''

correo = 'miSUPERagente@gmail-com,MICorreo@gmail-com,unaCUENtAmas@gmail-com'

correoCorregido = correo.replace('-','.').lower().split(',')
print(correoCorregido)
for c in correoCorregido:
    print(c)