def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input("ingrese un precio: "))
    print(f"Precio: {precio}")
    descuento = float(input("ingrese el descuento: "))
    print(f"Descuento: {descuento}")
    cantidad = int(input("ingrese cantidad"))
    print(f"Cantidad: {cantidad}")
    precio_descuento = precio *(1 - descuento / 100)
    print(f"Precio con descuento: {precio_descuento}")
    Total = precio_descuento * cantidad
    print(f"Total: {Total}")
#casting()


