def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = float(input("ingrese la base del rectangulo: "))
    altura = float(input("ingrese la altura: "))
    area = base*altura
    print("el area es: ", area)
    perimetro = base + base + altura + altura 
    print("el perimetro es: ", perimetro)
rectangle()
    
