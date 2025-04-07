class Cuadrado:
    def __init__(self,lado):
        self.lado = lado


        def area(self):
            return self.lado * self.lado

############################################################################################
lado = int(input("ingresa el lado"))
mi_ejemplo = Cuadrado(lado)
r = mi_ejemplo.area()
print(f"el area es {r}")
