class Vehiculo:
    def __init__(self, placa, marca):
        self.placa = placa
        self.marca = marca

    def mostrar(self):
        print(f"Placa: {self.placa} ({self.marca})")

class Automovil(Vehiculo):
    def dibujar(self):
        print("     ______")
        print(" ___/|_||_\\`.__")
        print("(   _    _ _\\")
        print("=`-(_)--(_)-'")

class Motocicleta(Vehiculo):
    def dibujar(self):
        print("     ,_oo")
        print("   _/  -\\_")
        print("  / \\  -  \\")
        print(" |   |    |")
        print("  \\_/\\___/")

class Camion(Vehiculo):
    def dibujar(self):
        print("  ____________________________")
        print(" |                            |____")
        print(" |    ____                    |    |")
        print(" |___|    |___________________|____|")
        print("       O                    O    O")

a = Automovil("ABC123", "Toyota")
m = Motocicleta("XYZ789", "Honda")
c = Camion("LMN456", "Volvo")

a.mostrar()
a.dibujar()
print("================================")
m.mostrar()
m.dibujar()
print("================================")
c.mostrar()
c.dibujar()