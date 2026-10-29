class Persona:
    def __init__(self,  documento, nombre):
        self.documento = documento
        self.nombre = nombre 

    def saludar(self):
        print(f"Hola, {self.nombre} Bienvenido")

class Estudiante(Persona):
    def matricular(self):
        print(f"El estudiante {self.nombre} se ha matriculado")

p = Estudiante(123456789, "Andres")
p.saludar()
p.matricular()