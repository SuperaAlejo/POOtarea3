from .base import Inmueble, Localizacion

class Local(Inmueble):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, localizacion: Localizacion):
        super().__init__(id_inmobiliario, area, direccion)
        self.localizacion = localizacion

    def imprimir(self):
        super().imprimir()
        print("Localización =", self.localizacion.value)

class LocalComercial(Local):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str,  localizacion: Localizacion, centro_comercial:str):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.centro_comercial = centro_comercial
        self.valor_area = 3000000

    def imprimir(self):
        super().imprimir()
        print("Centro comercial =", self.centro_comercial)


class Oficina(Local):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str,  localizacion: Localizacion, es_gobierno:bool):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.es_gobierno = es_gobierno
        self.valor_area = 3500000

    def imprimir(self):
        super().imprimir()
        print("Es del gobierno =", self.es_gobierno)
