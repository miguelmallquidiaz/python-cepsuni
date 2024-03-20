# Calculadora de IMC
# IMC = Peso (kg) / Altura * Altura (m)
#Clasificación de IMC

def calcularImc():
    imc = peso / (altura * altura)
    if imc < 18.5:
        resultado = 'Insuficiencia ponderal'
    elif imc < 24.9:
        resultado = 'Intervalo normal'
    elif imc < 29.9:
        resultado = 'Sobrepeso'
    else:
        resultado = 'Obesidad'
    print(f'El indice de masa coporal es {imc:.2f} y su clasificación es {resultado}')

peso = float((input('Ingrese su peso (kg): ')))
altura = float((input('Ingrese su altura(m): ')))

calcularImc()