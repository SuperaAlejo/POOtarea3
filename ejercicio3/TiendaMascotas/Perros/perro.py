from ..base import Mascota

class Perro(Mascota):
    def __init__(self, nombre:str, edad:int, color:str, peso:float, muerde:bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")