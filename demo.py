class Cuadrado:
    def __init__(self,lado):
        self.lado = lado


    def area(self):
            return self.lado **2

############################################################################################
lado = int(input("ingresa el lado"))
mi_ejemplo = Cuadrado(lado)
r = mi_ejemplo.area()
print(f"el area es {r}")
