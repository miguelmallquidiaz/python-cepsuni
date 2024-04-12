try:
    print('----------------------------------------------')
    print('|      CALIFICACIÓN FINAL DEL POSTULANTE     |')
    print('----------------------------------------------')
    
    pruebaActitud = int(input('Ingresar prueba de actitud.............: '))
    pruebaTeorica = int(input('Ingresar prueba de habilidad teórica...: '))
    pruebaPractica = int(input('Ingresar prueba de habilidad práctica..: '))
    entrevistaPersonal = int(input('Ingresar entrevista personal...........: '))

    resultado = pruebaActitud * 0.25 + (pruebaTeorica * 0.4 + pruebaPractica * 0.6) * 0.45 + entrevistaPersonal * 0.3
    
    print('\n----------------------------------------------')
    print('|                  RESULTADO                 |')
    print('----------------------------------------------')
    print('Calificación final....................: {:.2f}'.format(resultado))
    print('----------------------------------------------')
    print('Creado por: Miguel Mallqui Diaz')
    print('----------------------------------------------')
except:
    print('Ingresar correctamente los valores 🤨')