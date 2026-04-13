def string_methods():
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    # Strip
    print(f"Strip: {nombre.strip()}")
    print(f"Lstrip: {nombre.lstrip()}")
    print(f"Rstrip: {nombre.rstrip()}")

    # Mayúsculas, minúsculas, título
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")

    # Find
    print(f"Find: {frase.find('gran')}")

    # Replace
    print(f"Replace: {frase.replace('programacion', 'desarrollo')}")

    # Count
    print(f"Count: {frase.count('a')}")

    # in
    print(f"Contiene Python: {'Python' in frase}")
    print(f"Contiene Java: {'Java' in frase}")

    # Slicing
    palabra = frase[:6]  # "Python"
    print(f"Slice: {palabra}")
    print(f"Paso: {palabra[::2]}")
    print(f"Reverso: {palabra[::-1]}")

    # f-string
    print(f"Formato: {nombre.strip()} sabe {palabra}")

    # Multilínea
    print(multilinea)
#string_methods()