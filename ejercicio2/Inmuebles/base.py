from enum import Enum

class Localizacion(Enum):
    INTERNO = "Interno"
    CALLE = "Calle"

class Inmueble:
    def __init__(self, id_inmobiliario:int, area:int, direccion:str):
        self.id_inmobiliario = id_inmobiliario
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0.0

    def calcular_precio_venta(self, precio_m2):
        self.precio_venta = self.area * precio_m2

    def imprimir(self):
        print("Identificador inmobiliario =", self.id_inmobiliario)
        print("Area =", self.area)
        print("Dirección =", self.direccion)
        print("Precio de venta = $", self.precio_venta)