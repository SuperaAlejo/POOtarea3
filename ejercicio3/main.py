from TiendaMascotas.Perros.pequeños import Caniche
from TiendaMascotas.Gatos.pelo_largo import Himalayo
from TiendaMascotas.Perros.perro import Perro 
from TiendaMascotas.Gatos.gato import Gato

if __name__ == "__main__":
    # Crear un perro pequeño de raza Caniche
    perro1 = Caniche(nombre="Fido", edad=3, color="blanco", peso=5.0, muerde=False)
    print(f"Perro: {perro1.nombre}, Edad: {perro1.edad}, Color: {perro1.color}, Peso: {perro1.peso}kg, ¿Muerde?: {perro1.muerde}")
    Perro.sonido()

    print("")
    
    # Crear un gato de raza Himalayo (pelo largo)
    gato1 = Himalayo(nombre="Misha", edad=2, color="gris", altura_salto=1.2, longitud_salto=2.0)
    print(f"Gato: {gato1.nombre}, Edad: {gato1.edad}, Color: {gato1.color}, Altura de salto: {gato1.altura_salto}m, Longitud de salto: {gato1.longitud_salto}m")
    Gato.sonido()