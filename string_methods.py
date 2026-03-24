def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    print("Original:", nombre)

    print("strip():", nombre.strip())
    print("lstrip():", nombre.lstrip())
    print("rstrip():", nombre.rstrip())

    print("upper():", frase.upper())
    print("lower():", frase.lower())
    print("title():", frase.title())

    print("find('gran'):", frase.find("gran"))
    print("replace():", frase.replace("Python", "Java"))
    print("count('a'):", frase.count("a"))

    print("'Python' in frase:", "Python" in frase)

    print("slicing con paso [::2]:", frase[::2])
    print("reverso [::-1]:", frase[::-1])

    print(f"Mi lenguaje favorito es {frase[:6]}")

    print("String multilínea:")
    print(multilinea)

string_methods()
