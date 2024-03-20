from Persona import Persona

class Empleado(Persona):
    def __init__(self, nomrbe, apellido, dni, telefono, salario):
        super().__init__(nomrbe, apellido, dni, telefono)
        self.salario = salario