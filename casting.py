def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input())
    print(f"Precio: {precio}")
    descuento = float(input())
    print(f"Descuento: {descuento}")
    cantidad = int(input())
    precio_descuento = precio - descuento
    print(f"Precio con descuento: {precio_descuento}")
    Total = precio_descuento * cantidad
    print(f"Total: {Total}")
#casting()

