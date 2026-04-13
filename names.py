def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    completo = nombre + " " + apellido

    print("En minúsculas:", completo.lower())
    print("En título:", completo.title())
    print("En mayúsculas:", completo.upper())
    print("Con tabulador:", nombre + "\t" + apellido)
