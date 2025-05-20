from ..base import Mascota

class Gato(Mascota):
    def __init__(self, nombre:str, edad:int, color:str, altura_salto:float, longitud_salto:float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")