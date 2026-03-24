def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = float(input("ingrese un precio: "))
    print(precio)
    descuento = float(input("ingrese el descuento: "))
    print(descuento)
    cantidad = int(input("ingrese cantidad"))
    print(cantidad)
    precio_descuento = precio *(1 - descuento / 100)
    total = precio_descuento * cantidad
    print(total)
casting()


