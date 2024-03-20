diccionario = {
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
    "10": "diez",
}
numero = input('Ingrese un número del 1 a 10: ')

for i in numero:
    print(diccionario[i], end= " ")