def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("ingrese su nombre: ").lower()
    if 'a' in nombre or 'e' in nombre or 'i' in nombre or 'o' in nombre or 'u' in nombre:
      print("contiene vocal")
    else:
        print("no contiene vocal")
check_vowels()
    
