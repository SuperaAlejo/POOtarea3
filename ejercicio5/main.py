from Profesores import Profesor, ProfesorTitular

if __name__ == "__main__":
    profesores = [Profesor(), ProfesorTitular()]
    for profesor in profesores:
        profesor.imprimir()