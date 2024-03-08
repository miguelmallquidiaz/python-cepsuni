#😊 😜 🙁 😠
seguirChateando = True

def reemplazarTextoPorEmote():
    texto = input('>Escribe un texto: ')
    if(texto == 'salir'):
        seguirChateando = False
    texto = texto.replace(':)', '😊')
    texto = texto.replace('feliz', '😊')
    texto = texto.replace('broma', '😜')
    texto = texto.replace('enojado', '😠')
    texto = texto.replace('triste', '🙁')
    print(texto)
    
while seguirChateando:
    reemplazarTextoPorEmote()
    


