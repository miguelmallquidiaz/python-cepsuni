curso = 'mi cuRso Es python'
print(curso.capitalize())
print(curso.lower())
print(curso.upper())
print(curso.swapcase())
print(curso.title())

cadena1 = 'Python2024'

print(cadena1.isalnum())
print(cadena1.isalpha())
print(cadena1.isdigit())
print(cadena1.islower())
print(cadena1.isspace())
print(cadena1.isupper())

cadena7 = '\n \t Python     2024'
print(cadena7.strip())
cadena8 = 'Quien mal acaba mal acaba'
print(cadena8.replace('mal','bien'))

email = 'python@gmail.com'
print(email.split('@'))