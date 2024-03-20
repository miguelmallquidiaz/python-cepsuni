class Persona:
    def __init__(self, nomrbe, apellido, dni, telefono):
        self.nombre = nomrbe
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.dni