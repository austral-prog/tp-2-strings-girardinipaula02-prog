def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"

    print(texto[0:3])      # Awe
    print(texto[3:])       # some
    print(texto[:4])       # Awes
    print(texto[::2])      # Aeoe
    print(texto.lower())   # awesome

slice_simple()
