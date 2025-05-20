from Inmuebles.vivienda import CasaRural, Apartaestudio
from Inmuebles.local import Oficina
from Inmuebles.base import Localizacion

if __name__ == "__main__":
    casa_rural = CasaRural(1, 120, "Vereda El Sol", 3, 2, 2, 15, 1800)
    casa_rural.calcular_precio_venta(casa_rural.valor_area)
    casa_rural.imprimir()
    print("\n---\n")

    oficina = Oficina(2, 80, "Carrera 45 #12-34", Localizacion.INTERNO, True)
    oficina.calcular_precio_venta(oficina.valor_area)
    oficina.imprimir()
    print("\n---\n")

    apartaestudio = Apartaestudio(3, 45, "Calle 100 #20-15", 150000)
    apartaestudio.calcular_precio_venta(apartaestudio.valor_area)
    apartaestudio.imprimir()