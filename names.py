def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    completo = nombre + " " + apellido

    print(completo.lower())
    print(completo.title())
    print(completo.upper())
    print(f"\t{completo.lower()}")
#names()
