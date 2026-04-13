def change():
    print("Ingresar gasto:")
    gasto = float(input())

    print("Dinero recibido:")  # ← agregado el :
    dinero = int(input())

    vuelto = dinero - gasto

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
#change()