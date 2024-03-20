from Persona import Persona

class Cliente(Persona):
    def __init__(self, nomrbe, apellido, dni, telefono, categoria):
        super().__init__(nomrbe, apellido, dni, telefono)
        self.categoria = categoria