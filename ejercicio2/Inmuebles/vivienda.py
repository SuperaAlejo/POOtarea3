from .base import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int):
        super().__init__(id_inmobiliario, area, direccion)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos

    def imprimir(self):
        super().imprimir()
        print("Número de habitaciones =", self.num_habitaciones)
        print("Número de baños =", self.num_banos)


class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, num_pisos:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.num_pisos = num_pisos

    def imprimir(self):
        super().imprimir()
        print("Número de pisos =", self.num_pisos)


class CasaRural(Casa):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, num_pisos:int, distancia_cabecera:int, altitud:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud
        self.valor_area = 1500000

    def imprimir(self):
        super().imprimir()
        print("Distancia a cabecera municipal =", self.distancia_cabecera)
        print("Altitud =", self.altitud)


class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, num_pisos:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)

    def imprimir(self):
        super().imprimir()


class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, num_pisos:int, valor_administracion:int, tiene_piscina:bool,tiene_campo_deportivo:bool):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_administracion = valor_administracion
        self.tiene_piscina = tiene_piscina
        self.tiene_campo_deportivo = tiene_campo_deportivo
        self.areas_comunes = tiene_piscina or tiene_campo_deportivo
        self.valor_area = 2500000

    def imprimir(self):
        super().imprimir()
        print("Valor administración =", self.valor_administracion)
        print("Incluye áreas comunes =", self.areas_comunes)


class CasaIndependiente(CasaUrbana):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, num_pisos:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_area = 3000000

    def imprimir(self):
        super().imprimir()


class Apartamento(InmuebleVivienda):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, valor_administracion:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print("Valor administración =", self.valor_administracion)


class Apartaestudio(Apartamento):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, valor_administracion:int):
        super().__init__(id_inmobiliario, area, direccion, 1, 1, valor_administracion)
        self.valor_area = 1500000

    def imprimir(self):
        super().imprimir()


class ApartamentoFamiliar(Apartamento):
    def __init__(self, id_inmobiliario:int, area:int, direccion:str, num_habitaciones:int, num_banos:int, valor_administracion:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, valor_administracion)
        self.valor_area = 2000000

    def imprimir(self):
        super().imprimir()